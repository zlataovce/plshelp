import requests
import re


def latest_commit_github(repo, branch):
	url = "https://api.github.com/repos/" + repo + "/commits/" + branch
	r = requests.get(url).json()
	return r["sha"][:7]

def latest_build_jenkins(joburl, regex=False):
	url = joburl.rstrip("/") + "/lastSuccessfulBuild/api/json"
	try:
		r = requests.get(url).json()
	except requests.exceptions.ConnectionError:
		return None
	if regex is not False:
		return re.search(regex, r["artifacts"][0]["displayPath"]).group(0)
	else:
		return r["number"]

def latest_release_github(joburl):
	url = "https://api.github.com/repos/" + joburl + "/releases/latest"
	r = requests.get(url).json()
	return r["tag_name"]

def latest_paper_build(minecraft_ver):
	url = "https://papermc.io/api/v2/projects/paper/versions/" + minecraft_ver
	r = requests.get(url)
	if r.status_code == 200:
		return r.json()["builds"][-1]
	else:
		return None