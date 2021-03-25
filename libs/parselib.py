class Parse:
    def __init__(self, filename):
        with open("r", filename) as f:
            self.subject = f.readlines()

    def analysis(self):
        start_exception_linecnt = False
        exception_linecnt = 0
        results = {
            "plugins": [],
            "errors": []
        }
        for i in self.subject:
            if start_exception_linecnt is True:
                if exception_linecnt >= 6
                    results["errors"].append(i)
                    exception_linecnt += 1
                    continue
                else:
                    start_exception_linecnt = False
            if 'Starting minecraft server version' in i:
                results["minecraft_version"] = i.split("Starting minecraft server version ")[1]
            elif 'This server is running' in i and 'version' in i:
                results["server_software"] = i.split(" version ")[1].split(" (MC: ")[0]
            elif '] Loading ' in i:
                results["plugins"].append(i.split('] Loading ')[1])
            elif 'generated an exception' in i:
                results["errors"].append(i)
                start_exception_linecnt = True
                exception_linecnt = 0
        return results
