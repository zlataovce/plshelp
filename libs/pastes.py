from urllib.request import urlretrieve
import requests
from bs4 import BeautifulSoup
from libs.utils import check_filename


class Paste:
    def __init__(self, url):
        """Identifies a service used to share the logs. Downloads the file from the service."""
        self.url = url
        self.filename = check_filename()

    def identify(self):
        if self.url is None:
            return False
        if "https://paste.gg" in self.url and "raw" in self.url:
            urlretrieve(self.url, self.filename)
            return True
        elif "https://paste.gg" in self.url and "raw" not in self.url:
            url = self.pastegg()
            if url is False:
                return False
            else:
                urlretrieve(url, self.filename)
                return True
        elif "https://pastebin.com" in self.url:
            paste_id = self.url.split("pastebin.com/")[1]
            urlretrieve("https://pastebin.com/raw/" + paste_id, self.filename)
            return True
        else:
            return False

    def pastegg(self):
        r = requests.get(self.url).content
        soup = BeautifulSoup(r, "html.parser")
        try:
            return "https://paste.gg/" + soup.find("a", {"class": "is-pulled-right button"})['href']
        except TypeError:
            return False
