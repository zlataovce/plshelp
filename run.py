from flask import Flask, request, abort, Response, render_template
from libs.parselib import Parse
from libs.pastes import Paste
from json import dumps, loads
from os import remove
import requests

app = Flask('')

@app.route('/api/v1')
def parse():
    url = request.args.get("url")
    if Paste(url).identify() is False:
        return abort(400)
    parser = Parse("latest.log")
    data = dumps(parser.analysis(), indent=2)
    remove('latest.log')
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
        index()
    if request.method == "POST":
        if r.status_code != 400:
            re = r.json()
            return render_template("show.html", plugins=re["plugins"], errors=re["errors"], minecraft_version=re["minecraft_version"], server_software=re["server_software"], reload=re["reload"], needs_newer_java=re["needs_newer_java"])
        else:
            return "The paste URL was wrong!", 400


@app.route("/showv2", methods=["GET","POST"])
def showv2():
    if request.method == "GET":
        index2()
    if request.method == "POST":
        with open("latest.log", "w") as f:
            f.write(request.form.get("logfile"))
        parser = Parse("latest.log")
        re = parser.analysis()
        remove('latest.log')
        return render_template("show.html", plugins=re["plugins"], errors=re["errors"], minecraft_version=re["minecraft_version"], server_software=re["server_software"], reload=re["reload"], needs_newer_java=re["needs_newer_java"])


app.run(host="0.0.0.0", port=8080)
