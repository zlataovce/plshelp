from flask import Flask, request, abort, Response, render_template
from libs.parselib import Parse
from libs.pastes import Paste
from json import dumps, loads
from os import remove
import requests
from random import randint

app = Flask('')

@app.route('/api/v1')
def parse():
    url = request.args.get("url")
    paster = Paste(url)
    if paster.identify() is False:
        return abort(400)
    parser = Parse(paster.filename())
    data = dumps(parser.analysis(), indent=2)
    remove(paster.filename())
    return Response(data, mimetype='application/json')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/text")
def index2():
    return render_template("textupload.html")


@app.route("/show", methods=["GET","POST"])
def show():
    if request.method == "GET":
        if request.args.get("type") == "share":
            r = requests.get("https://plshelp.mkdev.ml/api/v1?url=" + request.args.get("url"))
            shareurl = "https://plshelp.mkdev.ml/show?type=share&url=" + request.args.get("url")
            if r.status_code != 400:
                re = r.json()
                return render_template("show.html", plugins=re["plugins"], errors=re["errors"], minecraft_version=re["minecraft_version"], server_software=re["server_software"], reload=re["reload"], needs_newer_java=re["needs_newer_java"], share_url=shareurl)
            else:
                return "The paste URL was wrong!", 400
    if request.method == "POST":
        r = requests.get("https://plshelp.mkdev.ml/api/v1?url=" + request.form.get("url"))
        shareurl = "https://plshelp.mkdev.ml/show?type=share&url=" + request.form.get("url")
        if r.status_code != 400:
            re = r.json()
            return render_template("show.html", plugins=re["plugins"], errors=re["errors"], minecraft_version=re["minecraft_version"], server_software=re["server_software"], reload=re["reload"], needs_newer_java=re["needs_newer_java"], share_url=shareurl)
        else:
            return "The paste URL was wrong!", 400


@app.route("/showv2", methods=["GET","POST"])
def showv2():
    if request.method == "GET":
        index2()
    if request.method == "POST":
        filename = "latest-" + str(randint(1, 100)) + ".log"
        with open(filename, "w") as f:
            f.write(request.form.get("logfile"))
        parser = Parse(filename)
        re = parser.analysis()
        remove(filename)
        try:
            return render_template("show.html", plugins=re["plugins"], errors=re["errors"], minecraft_version=re["minecraft_version"], server_software=re["server_software"], reload=re["reload"], needs_newer_java=re["needs_newer_java"], share_url="https://plshelp.mkdev.ml")
        except KeyError:
            return "Incomplete logs!", 400


app.run(host="0.0.0.0", port=8080)
