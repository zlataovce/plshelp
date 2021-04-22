from libs.apis import latest_build_jenkins, latest_release_github


def classify(gravity, lang, plugin, mcver, cfg):
    minecraft_versions = cfg["GENERAL"]["MinecraftVer"].split(",")
    plugin_class = gravity[plugin]  # gravity data for that plugin
    if "regex" in plugin_class:
        regex = plugin_class["regex"]
    else:
        regex = False
    # defined the regex
    if plugin_class["type"] == "normal":
        if "attribs" in plugin_class:
            plugin_attribs = []
            for i in plugin_class["attribs"]:
                plugin_attribs.append(lang["attribs"][i])  # appending attributes from lang to result
            if mcver not in plugin_class["ver"]:
                if minecraft_versions.index(mcver) - minecraft_versions.index(plugin_class["ver"][0]) < 0:
                    plugin_attribs.append(
                        lang["attribs"]["requiredver-newer"] + " (at least " + plugin_class["ver"][0] + ")")
                elif minecraft_versions.index(mcver) - minecraft_versions.index(plugin_class["ver"][0]) > 0:
                    plugin_attribs.append(
                        lang["attribs"]["requiredver-older"] + " (newest possible " + plugin_class["ver"][-1] + ")")
            if plugin_class["ci"] == "jenkins":
                return {"latest_build": latest_build_jenkins(plugin_class["link"], regex=regex),
                        "attributes": plugin_attribs}  # returning a dict with jenkins build and attribs
            elif plugin_class["ci"] == "github":
                return {"latest_build": latest_release_github(plugin_class["link"]),
                        "attributes": plugin_attribs}  # returning a dict with github release tag and attribs
        else:
            if plugin_class["ci"] == "jenkins":
                return {"latest_build": latest_build_jenkins(plugin_class["link"], regex=regex),
                        "attributes": None}  # returning a dict with github release tag and attribs
            elif plugin_class["ci"] == "github":
                return {"latest_build": latest_release_github(plugin_class["link"]),
                        "attributes": None}  # returning a dict with github release tag and attribs
    if plugin_class["type"] == "warn":
        return [plugin_class["desc"]]  # returning a list with warnings
