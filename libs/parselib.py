from configparser import ConfigParser

class Parse:
    def __init__(self, filename):
        with open(filename, "r") as f:
            self.subject = f.readlines()
        self.config = ConfigParser()
        self.config.read('config.ini')
        self.blacklist = self.config['PARSER']['WordIndexBlacklist'].split(",")
        self.errorblacklist = self.config['PARSER']['ErrorBlacklist'].split(",")
        self.errorwhitelist = self.config['PARSER']['ErrorWhitelist'].split(",")

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
                        if "\tat " in i or "java.lang" in i:
                            results["errors"].append(i.rstrip("\n").replace("\t", ""))
                            exception_linecnt += 1
                            continue
                        else:
                            start_exception_linecnt = False
                    else:
                        start_exception_linecnt = False
                if 'Starting minecraft server version' in i:
                    results["minecraft_version"] = i.split("Starting minecraft server version ")[1].rstrip("\n")
                elif 'This server is running' in i and 'version' in i:
                    results["server_software"] = i.split(" version ")[1].split(" (MC: ")[0].rstrip("\n")
                elif '] Loading ' in i and " v" in i:
                    try:
                        for x in self.blacklist:
                            if x in i:
                                raise ValueError
                        if i.split('] Loading ')[1].rstrip("\n") in results["plugins"]:
                            continue
                        results["plugins"].append(i.split('] Loading ')[1].rstrip("\n"))
                    except ValueError:
                        continue
                elif 'generated an exception' in i or "Could not pass event" in i or 'Exception' in i or "Could not load '" in i:
                    try:
                        for x in self.errorblacklist:
                            if x in i:
                                raise ValueError
                        results["errors"].append(i.rstrip("\n").replace("\t", ""))
                        start_exception_linecnt = True
                        exception_linecnt = 0
                    except ValueError:
                        continue
                elif 'Server thread/ERROR' in i:
                    try:
                        for x in self.errorblacklist:
                            if x in i:
                                raise ValueError
                        results["errors"].append(i.rstrip("\n"))
                    except ValueError:
                        continue
                elif '/rl' in i or '/reload' in i:
                    results['reload'] = True
                elif 'UnsupportedClassVersionError' in i and 'this version of the Java Runtime only recognizes class file versions up to 52.0' in i:
                    results['needs_newer_java'] = True
                elif 'Server thread/WARN' in i:
                    for x in self.errorwhitelist:
                        if x in i:
                            results["errors"].append(i.rstrip("\n"))

                if 'Wrong shop.yml/shop.groovy configuration!' in i:
                    results["sbw_wrongshop"] = True
            except AttributeError:
                continue
        try:
            if results['needs_newer_java'] is True:
                pass
        except KeyError:
            results['needs_newer_java'] = False
        try:
            if results['reload'] is True:
                pass
        except KeyError:
            results['reload'] = False
        try:
            if results['sbw_wrongshop'] is True:
                pass
        except KeyError:
            results['sbw_wrongshop'] = False
        return results
