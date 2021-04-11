from libs.apis import latest_build_jenkins, latest_release_github


def classify(gravity, lang, plugin):
	plugin_class = gravity[plugin]
	if "regex" in plugin_class:
		regex = plugin_class["regex"]
	else:
		regex = False
	if plugin_class["type"] == "normal":
		if "attribs" in plugin_class:
			plugin_attribs = []
			for i in plugin_class["attribs"]:
				plugin_attribs.append(lang["attribs"][i])
			if plugin_class["ci"] == "jenkins":
				return {"latest_build": latest_build_jenkins(plugin_class["link"], regex=regex), "attributes": plugin_attribs}
			elif plugin_class["ci"] == "github":
				return {"latest_build": latest_release_github(plugin_class["link"]), "attributes": plugin_attribs}
		else:
			if plugin_class["ci"] == "jenkins":
				return {"latest_build": latest_build_jenkins(plugin_class["link"], regex=regex), "attributes": None}
			elif plugin_class["ci"] == "github":
				return {"latest_build": latest_release_github(plugin_class["link"]), "attributes": None}
	if plugin_class["type"] == "warn":
		return [plugin_class["desc"]]