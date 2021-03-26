class Parse:
    def __init__(self, filename):
        with open(filename, "r") as f:
            self.subject = f.readlines()

    def analysis(self):
        start_exception_linecnt = False
        exception_linecnt = 0
        results = {
            "plugins": [],
            "errors": []
        }
        for i in self.subject:
            try:
                if start_exception_linecnt is True:
                    if exception_linecnt <= 6:
                        results["errors"].append(i.rstrip("\n").replace("\t", ""))
                        exception_linecnt += 1
                        continue
                    else:
                        start_exception_linecnt = False
                if 'Starting minecraft server version' in i:
                    results["minecraft_version"] = i.split("Starting minecraft server version ")[1].rstrip("\n")
                elif 'This server is running' in i and 'version' in i:
                    results["server_software"] = i.split(" version ")[1].split(" (MC: ")[0].rstrip("\n")
                elif '] Loading ' in i and " v" in i:
                    results["plugins"].append(i.split('] Loading ')[1].rstrip("\n"))
                elif 'generated an exception' in i or 'Server thread/ERROR' in i:
                    results["errors"].append(i.rstrip("\n").replace("\t", ""))
                    start_exception_linecnt = True
                    exception_linecnt = 0
            except AttributeError:
                continue
        return results
