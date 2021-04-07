from os.path import exists
from random import randint


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
