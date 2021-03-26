from flask import Flask, request, abort
from libs.parselib import Parse
from libs.pastes import Paste
from json import dumps
from os import remove

app = Flask('')

@app.route('/v1')
def parse():
    url = request.args.get("url")
    if Paste(url).identify() is False:
        return abort(400)
    parser = Parse("latest.log")
    data = dumps(parser.analysis(), indent=2)
    remove('latest.log')
    return data

app.run(host="0.0.0.0", port=8080)
