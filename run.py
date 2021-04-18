import concurrent.futures
import datetime
from configparser import ConfigParser
from json import dumps
from os import environ
from sys import argv

from dotenv import load_dotenv
from flask import Flask, request, Response, render_template
from pbwrap import Pastebin

import libs.exceptions
from libs.apis import latest_paper_build
from libs.classifylib import classify
from libs.parselib import Parse
from libs.pastes import Paste
from libs.utils import sanitize, jsonf, fetch_updates, Debugger

load_dotenv()  # loading the .env

app = Flask('')  # making the flask app

config = ConfigParser()
config.read('config.ini')  # reading the config.ini

d = Debugger()  # making the debugger
d.state = config["GENERAL"].getboolean("Debugger")  # debugger state from config

if config["UPDATE"].getboolean("GravityAutoUpdate"):
    fetch_updates(config["UPDATE"]["GravityFile"], config["UPDATE"]["LangFile"])  # fetching the updates if autoupdate is enabled

# loading the json files
gravity = jsonf("gravity.json")
lang = jsonf("lang.json")


# webresponse=True makes the functions return a Flask Response object
def parsev1(url, webresponse=True):
    global d
    d.dprint("QUERY: Started processing")
    time = datetime.datetime.now()  # measuring the time for the debugger, gonna integrate this into the debugger later
    paster = Paste(url)
    file = paster.identify()  # identyfing the paste url and getting it
    if file is False:
        if webresponse:
            return "Needs URL parameter or specified URL isn't a paste.gg/pastebin.com URL.", 400  # webresponse error
        else:
            raise libs.exceptions.InvalidURL  # raising an exception for invalid url
    d.dprint("QUERY: Started analysis")
    time_analysis = datetime.datetime.now()
    data = Parse(file).analysis()  # performing the analysis
    d.dprint("QUERY: Analysis finished in " + str(round((datetime.datetime.now() - time_analysis).microseconds / 1000)) + " milliseconds")  # printing the debugger data
    time_elapsed = datetime.datetime.now() - time
    if webresponse:
        d.dprint("QUERY: Processed in " + str(time_elapsed.seconds) + " seconds")
        return Response(dumps(data, indent=2), mimetype='application/json')  # returning a Flask Response object
    else:
        d.dprint("QUERY: Processed in " + str(time_elapsed.seconds) + " seconds")
        return data  # returning a dict


def parsev2(url, webresponse=True, directfile=False):  # api v2
    global gravity, lang, d
    d.dprint("QUERY: Started processing")
    time = datetime.datetime.now()
    if directfile is True:
        data = Parse(url).analysis()  # only analysing if directfile=True
    else:
        paster = Paste(url)
        file = paster.identify()  # getting the paste
        if file is False:
            d.dprint("QUERY: Invalid paste.gg URL while handling")
            raise libs.exceptions.InvalidURL  # raising an exception
        d.dprint("QUERY: Started analysis")
        time_analysis = datetime.datetime.now()
        data = Parse(file).analysis()  # performing the analysis
        d.dprint("QUERY: Analysis finished in " + str(round((datetime.datetime.now() - time_analysis).microseconds / 1000)) + " milliseconds")
    data["gravity_classified_plugins"] = {}
    for i in gravity.keys():  # classifying the plugins by gravity
        if i in data["plugins_altver"]:
            r = classify(gravity, lang, i)
            # changing the layout of the dict
            if isinstance(r, dict):
                data["gravity_classified_plugins"][i] = r
            elif isinstance(r, list):
                data["gravity_classified_plugins"][i] = {"latest_build": None, "attributes": r}
    if data["server_software"] is not None:  # getting the latest build of Paper
        if "Paper" in data["server_software"]:
            data["paper_build"] = latest_paper_build(data["minecraft_version"])
        else:
            data["paper_build"] = None
    else:
        data["paper_build"] = None
    time_elapsed = datetime.datetime.now() - time
    if webresponse:
        d.dprint("QUERY: Finished processing, returning webresponse")
        d.dprint("QUERY: Processed in " + str(time_elapsed.seconds) + " seconds")
        return Response(dumps(data, indent=2), mimetype='application/json')
    else:
        d.dprint("QUERY: Finished processing, returning data")
        d.dprint("QUERY: Processed in " + str(time_elapsed.seconds) + " seconds")
        return data


# @app.errorhandler(404)
# def page_not_found(e):
#     config = ConfigParser()
#     config.read('config.ini')
#     # note that we set the 404 status explicitly
#     return render_template('templates/404.html', domain=config['FLASK']['Domain']), 404

# uploading a file to pastebin, recommended to invoke it as a thread using ThreadPoolExecutor
def upload_paste_thread(text):
    global config
    pb = Pastebin(api_dev_key=environ.get('PASTEBIN_API_KEY'))
    pasteurl = pb.create_paste(text, api_paste_expire_date=config['SHARE']['PasteExpire'],
                               api_paste_name=config['SHARE']['PasteTitle'])
    if "Bad API request" in pasteurl:
        pasteurl = "Upload error"
    return pasteurl


# a flask wrapper for the api function
@app.route('/api/v1')
def web_parsev1():
    return parsev1(request.args.get("url"))


# a flask wrapper for the api function
@app.route('/api/v2')
def web_parsev2():
    return parsev2(request.args.get("url"))


# a flask wrapper for the index.html template
@app.route("/")
def index():
    global config
    return render_template("index.html", domain=config['FLASK']['Domain'])


# a flask wrapper for the textupload.html template
@app.route("/text")
def index2():
    global config
    return render_template("textupload.html", domain=config['FLASK']['Domain'])


# a flask wrapper for the loglist.html template
@app.route("/logs")
def loglist():
    global config
    return render_template("loglist.html", domain=config['FLASK']['Domain'])


# a flask wrapper for the show.html template
# noinspection PyTypeChecker
@app.route("/show", methods=["GET", "POST"])
def show():
    global config
    if request.method == "GET":  # only for sharing
        try:
            re = parsev2(request.args.get("url"), webresponse=False)  # getting the data
        except libs.exceptions.InvalidURL:
            return "Needs URL parameter or specified URL isn't a paste.gg/pastebin.com URL.", 400
        shareurl = config['FLASK']['Domain'] + "/show?type=share&url=" + request.args.get("url")
        if request.args.get("type") == "share":
            return render_template("show.html", plugins=re["plugins"], classifiederrors=re["classified_errors"],
                                   minecraft_version=re["minecraft_version"], server_software=re["server_software"],
                                   reload=re["reload"], needs_newer_java=re["needs_newer_java"], share_url=shareurl,
                                   sbw_wrongshop=re["sbw_wrongshop"], paste_url=request.args.get("url"),
                                   domain=config['FLASK']['Domain'], errors=re["errors"],
                                   gravityplugins=re["gravity_classified_plugins"], paperbuild=re["paper_build"])
    if request.method == "POST":
        try:
            re = parsev2(request.form.get("url"), webresponse=False)  # getting the data
        except libs.exceptions.InvalidURL:
            return "Needs URL parameter or specified URL isn't a paste.gg/pastebin.com URL.", 400
        shareurl = config['FLASK']['Domain'] + "/show?type=share&url=" + request.form.get("url")
        return render_template("show.html", plugins=re["plugins"], classifiederrors=re["classified_errors"],
                               minecraft_version=re["minecraft_version"], server_software=re["server_software"],
                               reload=re["reload"], needs_newer_java=re["needs_newer_java"], share_url=shareurl,
                               sbw_wrongshop=re["sbw_wrongshop"], paste_url=request.form.get("url"),
                               domain=config['FLASK']['Domain'], errors=re["errors"],
                               gravityplugins=re["gravity_classified_plugins"], paperbuild=re["paper_build"])


# a flask wrapper for the show.html template with a different input method
# noinspection PyTypeChecker
@app.route("/showv2", methods=["GET", "POST"])
def showv2():
    global config, gravity, lang
    if request.method == "GET":
        return index2()
    if request.method == "POST":
        with concurrent.futures.ThreadPoolExecutor() as executor:  # uploading the POSTed log to pastebin
            thread = executor.submit(upload_paste_thread, sanitize(request.form.get("logfile")))
        try:
            re = parsev2(sanitize(request.form.get("logfile")).splitlines(), webresponse=False, directfile=True)  # meanwhile analysing the file
        except libs.exceptions.InvalidURL:
            return "Needs URL parameter or specified URL isn't a paste.gg/pastebin.com URL.", 400
        pasteurl = thread.result()  # getting the pastebin url from the thread
        shareurl = config['FLASK']['Domain'] + "/show?type=share&url=" + pasteurl
        try:
            return render_template("show.html", plugins=re["plugins"], classifiederrors=re["classified_errors"],
                                   minecraft_version=re["minecraft_version"], server_software=re["server_software"],
                                   reload=re["reload"], needs_newer_java=re["needs_newer_java"], share_url=shareurl,
                                   sbw_wrongshop=re["sbw_wrongshop"], paste_url=pasteurl,
                                   domain=config['FLASK']['Domain'], errors=re["errors"],
                                   gravityplugins=re["gravity_classified_plugins"], paperbuild=re["paper_build"])
        except KeyError:
            return "Incomplete logs!", 400

try:
    if argv[1] == 'heroku':
        app.run(host="0.0.0.0", port=environ.get("PORT"))  # running the flask app
    else:
        app.run(host="0.0.0.0", port=8080)  # running the flask app
except IndexError:
    app.run(host="0.0.0.0", port=8080)  # running the flask app
