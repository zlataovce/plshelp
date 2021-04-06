from flask import Flask, request, Response, render_template
from libs.parselib import Parse
from libs.pastes import Paste
from json import dumps
from os import remove, environ
import requests
from pbwrap import Pastebin
from dotenv import load_dotenv
from libs.utils import check_filename
from configparser import ConfigParser
import concurrent.futures

load_dotenv()

app = Flask('')

config = ConfigParser()
config.read('config.ini')

##@app.errorhandler(404)
##def page_not_found(e):
##    config = ConfigParser()
##    config.read('config.ini')
##    # note that we set the 404 status explicitly
##    return render_template('templates/404.html', domain=config['FLASK']['Domain']), 404


def upload_paste_thread(text):
    global config
    pb = Pastebin(api_dev_key=environ.get('PASTEBIN_API_KEY'))
    pasteurl = pb.create_paste(text, api_paste_expire_date=config['SHARE']['PasteExpire'],
                               api_paste_name=config['SHARE']['PasteTitle'])
    if "Bad API request" in pasteurl:
        pasteurl = "Upload error"
    return pasteurl


@app.route('/api/v1')
def parse():
    url = request.args.get("url")
    paster = Paste(url)
    if paster.identify() is False:
        return "Needs URL parameter or specified URL isn't a paste.gg/pastebin.com URL.", 400
    parser = Parse(paster.filename)
    data = dumps(parser.analysis(), indent=2)
    remove(paster.filename)
    return Response(data, mimetype='application/json')


@app.route("/")
def index():
    global config
    return render_template("index.html", domain=config['FLASK']['Domain'])


@app.route("/text")
def index2():
    global config
    return render_template("textupload.html", domain=config['FLASK']['Domain'])

@app.route("/logs")
def loglist():
    global config
    return render_template("loglist.html", domain=config['FLASK']['Domain'])


@app.route("/show", methods=["GET", "POST"])
def show():
    global config
    if request.method == "GET":
        if request.args.get("type") == "share":
            r = requests.get(config['FLASK']['Domain'] + "/api/v1?url=" + request.args.get("url"))
            shareurl = config['FLASK']['Domain'] + "/show?type=share&url=" + request.args.get("url")
            if r.status_code != 400:
                re = r.json()
                return render_template("show.html", plugins=re["plugins"], errors=re["errors"],
                                       minecraft_version=re["minecraft_version"], server_software=re["server_software"],
                                       reload=re["reload"], needs_newer_java=re["needs_newer_java"], share_url=shareurl,
                                       sbw_wrongshop=re["sbw_wrongshop"], paste_url=request.args.get("url"), domain=config['FLASK']['Domain'])
            else:
                return "The paste URL was wrong!", 400
    if request.method == "POST":
        r = requests.get(config['FLASK']['Domain'] + "/api/v1?url=" + request.form.get("url"))
        shareurl = config['FLASK']['Domain'] + "/show?type=share&url=" + request.form.get("url")
        if r.status_code != 400:
            re = r.json()
            return render_template("show.html", plugins=re["plugins"], errors=re["errors"],
                                   minecraft_version=re["minecraft_version"], server_software=re["server_software"],
                                   reload=re["reload"], needs_newer_java=re["needs_newer_java"], share_url=shareurl,
                                   sbw_wrongshop=re["sbw_wrongshop"], paste_url=request.form.get("url"), domain=config['FLASK']['Domain'])
        else:
            return "The paste URL was wrong!", 400


@app.route("/showv2", methods=["GET", "POST"])
def showv2():
    global config
    if request.method == "GET":
        index2()
    if request.method == "POST":
        filename = check_filename()
        with open(filename, "w") as f:
            f.write(request.form.get("logfile"))
        with concurrent.futures.ThreadPoolExecutor() as executor:
            thread = executor.submit(upload_paste_thread, request.form.get("logfile"))
        parser = Parse(filename)
        re = parser.analysis()
        pasteurl = thread.result()
        shareurl = config['FLASK']['Domain'] + "/show?type=share&url=" + pasteurl
        remove(filename)
        try:
            return render_template("show.html", plugins=re["plugins"], errors=re["errors"],
                                   minecraft_version=re["minecraft_version"], server_software=re["server_software"],
                                   reload=re["reload"], needs_newer_java=re["needs_newer_java"], share_url=shareurl,
                                   sbw_wrongshop=re["sbw_wrongshop"], paste_url=pasteurl, domain=config['FLASK']['Domain'])
        except KeyError:
            return "Incomplete logs!", 400


app.run(host="0.0.0.0", port=8080)
