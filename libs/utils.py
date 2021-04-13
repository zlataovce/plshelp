from json import load
from os import remove
from os.path import exists
from urllib.request import urlretrieve


def sanitize(text):  # saniting the pastes, because why not xd, i don't want errors
    to_sanitize = ["✘", "\\", "❤", "✔"]
    for i in to_sanitize:
        text = text.replace(i, "")
    return text


def jsonf(filename):  # a function for opening a json file by the filename (json module doesn't apparently have this)
    with open(filename, "r") as f:
        return load(f)


def fetch_updates(gravity_file, lang_file):  # fetching updates for the gravity and lang files
    if exists(gravity_file):
        remove(gravity_file)
        urlretrieve("https://raw.githubusercontent.com/zlataovce/plshelp/main/gravity.json", gravity_file)
        print("Updated the gravity file!")
    else:
        urlretrieve("https://raw.githubusercontent.com/zlataovce/plshelp/main/gravity.json", gravity_file)
        print("Downloaded the gravity file!")
    if exists(lang_file):
        remove(lang_file)
        urlretrieve("https://raw.githubusercontent.com/zlataovce/plshelp/main/lang.json", lang_file)
        print("Updated the language file!")
    else:
        urlretrieve("https://raw.githubusercontent.com/zlataovce/plshelp/main/lang.json", lang_file)
        print("Downloaded the language file!")


class Debugger:  # a simple print() debugger, toggleable
    def __init__(self):
        self.state = False

    def dprint(self, v):
        if self.state is True:
            print(v)
