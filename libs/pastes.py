import requests
from bs4 import BeautifulSoup


class Paste:
    def __init__(self, url):
        """Identifies a service used to share the logs. Downloads the file from the service."""
        self.url = url

    def identify(self):
        if self.url is None:
            return False
        if self.url.startswith("https://paste.gg") and "raw" in self.url:
            r = requests.get(self.url)
            return r.text.splitlines()
        elif self.url.startswith("https://paste.gg") and "raw" not in self.url:
            url = self.pastegg()
            if url is False:
                return False
            else:
                r = requests.get(url)
                return r.text.splitlines()
        elif self.url.startswith("https://pastebin.com"):
            paste_id = self.url.split("pastebin.com/")[1]
            r = requests.get("https://pastebin.com/raw/" + paste_id)
            return r.text.splitlines()
        else:
            return False

    def pastegg(self):
        r = requests.get(self.url)
        if not r.ok:
            return False
        soup = BeautifulSoup(r.content, "html.parser")
        try:
            return "https://paste.gg/" + soup.find("a", {"class": "is-pulled-right button"})['href']
        except TypeError:
            return False
