from flask import Flask, request
from libs.parselib import Parse
from libs.pastes import Paste
from json import dumps

app = Flask('')

@app.route('/v1')
def parse():
    url = request.args.get("url")
    if Paste(url).identify() is False:
        return {}
    parser = Parse("latest.log")
    return dumps(parser.analysis(), indent=2)

app.run(host="0.0.0.0", port=8080)
