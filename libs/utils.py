from os.path import exists
from os import remove
from random import randint
from json import load
from urllib.request import urlretrieve


def check_filename():
    filename = "latest-" + str(randint(1, 1000)) + ".log"
    if exists(filename):
        while True:
            filename = "latest-" + str(randint(1, 1000)) + ".log"
            if not exists(filename):
                return filename
    else:
        return filename


def sanitize(text):
    to_sanitize = ["✘", "\\", "❤", "✔"]
    for i in to_sanitize:
        text = text.replace(i, "")
    return text


def jsonf(filename):
    with open(filename, "r") as f:
        return load(f)


def fetch_updates(gravity_file, lang_file):
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
