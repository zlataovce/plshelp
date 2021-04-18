from configparser import ConfigParser


# noinspection PyTypeChecker
class Parse:
    def __init__(self, content):
        """Parses the minecraft logs and returns the results in a dict."""
        self.subject = content
        self.config = ConfigParser()
        self.config.read('config.ini')  # reading config
        # loading blacklists/whitelists
        self.blacklist = self.config['PARSER']['WordIndexBlacklist'].split(",")
        self.errorblacklist = self.config['PARSER']['ErrorBlacklist'].split(",")
        self.errorwhitelist = self.config['PARSER']['ErrorWhitelist'].split(",")
        self.crackedkeywords = self.config['PARSER']['CrackedPluginKeywords'].split(",")
        self.results = {
            "plugins": [],
            "plugins_altver": [],
            "errors": [],
            "classified_errors": {}
        }  # premature results defining

    def analysis(self):
        start_exception_linecnt = False  # this is just including the lines of exceptions
        exception_linecnt = 0  # for counting the lines of exceptions
        for i in self.subject:
            try:
                if start_exception_linecnt is True:  # ignoring classifying and just appending the lines
                    # if they are a part of an exception
                    if exception_linecnt <= 6:
                        if "at " in i or "java.lang" in i:
                            self.results["errors"].append(i.rstrip("\n").replace("\t", ""))
                            exception_linecnt += 1
                            continue
                        else:
                            start_exception_linecnt = False
                    else:
                        start_exception_linecnt = False
                if 'Starting minecraft server version' in i:
                    self.results["minecraft_version"] = i.split("Starting minecraft server version ")[1].rstrip("\n")  # getting the minecraft version
                elif 'This server is running' in i and 'version' in i:
                    self.results["server_software"] = i.split(" version ")[1].split(" (MC: ")[0].rstrip("\n")  # getting the server software version
                elif '] Loading ' in i and " v" in i:
                    try:
                        for x in self.blacklist:  # reading words blacklisted from classifying as plugins, thanks bw1069 for the FP's
                            if x in i:
                                raise ValueError
                        if i.split('] Loading ')[1].rstrip("\n") in self.results["plugins"]:  # no duplicated plugins
                            continue
                        if i.split('] Loading ')[1].split(' v')[0].rstrip("\n") in self.results["plugins_altver"]:  # no duplicated plugins
                            continue
                        self.results["plugins"].append(i.split('] Loading ')[1].rstrip("\n"))  # appending the plugin
                        self.results["plugins_altver"].append(i.split('] Loading ')[1].split(' v')[0].rstrip("\n"))  # appending the plugin
                    except ValueError:  # used as a continue for nested for loops
                        continue
                elif 'generated an exception' in i or "Could not pass event" in i or 'Exception' in i or "Could not " \
                                                                                                         "load '" in i:  # reading blacklisted exceptions
                    try:
                        for x in self.errorblacklist:  # reading blacklisted exceptions
                            if x in i:
                                raise ValueError
                        self.results["errors"].append(i.rstrip("\n").replace("\t", ""))  # appending the exception
                        start_exception_linecnt = True
                        exception_linecnt = 0
                        # starting the count
                    except ValueError:  # used as a continue for nested for loops
                        continue
                elif 'Server thread/ERROR' in i:
                    try:
                        for x in self.errorblacklist:  # reading blacklisted errors
                            if x in i:
                                raise ValueError
                        self.results["errors"].append(i.rstrip("\n"))  # appending the error
                    except ValueError:  # used as a continue for nested for loops
                        continue
                elif '/rl' in i or '/reload' in i:
                    self.results['reload'] = True  # did the server reload?
                elif 'UnsupportedClassVersionError' in i and 'this version of the Java Runtime only recognizes class ' \
                                                             'file versions up to 52.0' in i:  # catching java 11 errors
                    self.results['needs_newer_java'] = True
                elif 'Server thread/WARN' in i:  # catching whitelisted warnings
                    for x in self.errorwhitelist:
                        if x in i:
                            self.results["errors"].append(i.rstrip("\n"))  # appending the item

                if 'Wrong shop.yml/shop.groovy configuration!' in i:
                    self.results["sbw_wrongshop"] = True  # sbw extension
                for x in self.crackedkeywords:  # checking if line contains keywords from cracked plugins
                    if x in i:
                        self.results["cracked_plugins"] = True
            except AttributeError:
                continue
        # setting defaults for unfilled results
        self.check_defaults_bool('needs_newer_java')
        self.check_defaults_bool('reload')
        self.check_defaults_bool('sbw_wrongshop')
        self.check_defaults_bool('cracked_plugins')
        self.check_defaults('minecraft_version', None)
        self.check_defaults('server_software', None)
        for i in self.results["plugins_altver"]:
            self.results["classified_errors"][i] = []  # making defaults for classified_errors
        for i in self.results["plugins_altver"]:
            start_exception_linecnt = False
            exception_linecnt = 0
            # classifying the errors by detecting a plugin name in the exception names
            for x in self.results["errors"]:  # counting the exception lines again
                if start_exception_linecnt is True:
                    if exception_linecnt <= 6:
                        if "at " in x or "java.lang" in x:
                            self.results["classified_errors"][i].append(x)
                            exception_linecnt += 1
                        else:
                            start_exception_linecnt = False
                    else:
                        start_exception_linecnt = False
                else:
                    if i in x:
                        try:
                            for y in self.errorblacklist:  # reading blacklisted errors
                                if y in x:
                                    raise ValueError
                            self.results["classified_errors"][i].append(x)  # adding the error as classified
                            if 'generated an exception' in x or "Could not pass event" in x or 'Exception' in x or "Could not load " in x:
                                if start_exception_linecnt is not True:  # detecting exceptions
                                    start_exception_linecnt = True
                                    exception_linecnt = 0
                        except ValueError:
                            pass
        for key, value in self.results["classified_errors"].items():  # setting defaults for unfilled results
            if not len(value):
                self.results["classified_errors"][key] = None
        return self.results

    # functions below are for setting defaults
    def check_defaults_bool(self, value):
        try:
            if self.results[value] is True:
                pass
        except KeyError:
            self.results[value] = False

    def check_defaults(self, value, defaults):
        try:
            if self.results[value] is not None:
                pass
        except KeyError:
            self.results[value] = defaults
