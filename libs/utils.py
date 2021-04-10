from os.path import exists
from random import randint
from json import load


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
    return text.replace("\\", "").replace("❤", "")


def jsonf(filename):
	with open(filename, "r") as f:
		return json.load(f)
