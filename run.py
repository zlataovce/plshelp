from flask import Flask, request, abort, Response, render_template
from libs.parselib import Parse
from libs.pastes import Paste
from json import dumps
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


@app.route("/show", methods=["GET","POST"])
def show():
    if request.method == "GET":
        index()
    if request.method == "POST":
        r = requests.get("https://plshelp.mkdev.ml/api/v1?url={0}".format(request.form.get("url")))
        if r.status_code != 400:
            re = r.json()
            return render_template("show.html", plugins=re["plugins"], errors=re["errors"], minecraft_version=re["minecraft_version"], server_software=re["server_software"], reload=re["reload"], needs_newer_java=re["needs_newer_java"])
        else:
            return "The paste URL was wrong!", 400


app.run(host="0.0.0.0", port=8080)
