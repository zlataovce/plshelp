from urllib.request import urlretrieve
import requests
from bs4 import BeautifulSoup

class Paste:
    def __init__(self, url):
        self.url = url

    def identify(self):
        if self.url is None:
            return False
        if "https://paste.gg" in self.url and "raw" in self.url:
            urlretrieve(self.url, "latest.log")
            return True
        elif "https://paste.gg" in self.url and not "raw" in self.url:
            urlretrieve(self.pastegg(), "latest.log")
            return True
        elif "https://pastebin.com" in self.url:
            id = self.url.split("pastebin.com/")[1]
            urlretrieve("https://pastebin.com/raw/" + id, "latest.log")
            return True
        else:
            return False

    def pastegg(self):
        r = requests.get(self.url).content
        soup = BeautifulSoup(r, "html.parser")
        return "https://paste.gg/" + soup.find("a", {"class": "is-pulled-right button"})['href']