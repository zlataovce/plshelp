import requests


class Paste:
    def __init__(self, url):
        """Identifies a service used to share the logs. Downloads the file from the service."""
        self.url = url

    def identify(self):
        if self.url is None:
            return False
        if self.url.startswith("https://paste.gg/") and "raw" in self.url:
            r = requests.get(self.url)
            return r.text.splitlines()
        elif self.url.startswith("https://paste.gg/") and "raw" not in self.url:
            if "/p/" in self.url:
                if "https" in self.url:
                    pasteid = self.url.replace("https://paste.gg/p/", "").split("/")[1]
                else:
                    pasteid = self.url.replace("http://paste.gg/p/", "").split("/")[1]
            else:
                if "https" in self.url:
                    pasteid = self.url.replace("https://paste.gg/", "")
                else:
                    pasteid = self.url.replace("http://paste.gg/", "")

            r = requests.get("https://api.paste.gg/v1/pastes/" + pasteid)
            if not r.ok:
                return False
            fileid = r.json()["result"]["files"][0]["id"]

            r2 = requests.get("https://api.paste.gg/v1/pastes/" + pasteid + "/files/" + fileid + "/raw")
            return r2.text.splitlines()
        elif self.url.startswith("https://pastebin.com/"):
            paste_id = self.url.split("pastebin.com/")[1]
            r = requests.get("https://pastebin.com/raw/" + paste_id)
            return r.text.splitlines()
        else:
            return False
