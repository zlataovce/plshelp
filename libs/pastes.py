from urllib.request import urlretrieve
import requests
from bs4 import BeautifulSoup
from libs.utils import check_filename


class Paste:
    def __init__(self, url):
        """Identifies a service used to share the logs. Downloads the file from the service."""
        self.url = url

    def identify(self):
        if self.url is None:
            return False
        if "https://paste.gg" in self.url and "raw" in self.url:
            r = requests.get(self.url)
            return r.text.splitlines()
        elif "https://paste.gg" in self.url and "raw" not in self.url:
            url = self.pastegg()
            if url is False:
                return False
            else:
                r = requests.get(url)
                return r.text.splitlines()
        elif "https://pastebin.com" in self.url:
            paste_id = self.url.split("pastebin.com/")[1]
            r = requests.get("https://pastebin.com/raw/" + paste_id)
            return r.text.splitlines()
        else:
            return False

    def pastegg(self):
        r = requests.get(self.url).content
        soup = BeautifulSoup(r, "html.parser")
        try:
            return "https://paste.gg/" + soup.find("a", {"class": "is-pulled-right button"})['href']
        except TypeError:
            return False
