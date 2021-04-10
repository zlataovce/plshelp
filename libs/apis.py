from requests import get

def latest_commit_github(repo, branch):
	url = "https://api.github.com/repos/" + repo + "/commits/" + branch
	r = get(url).json()
	return r["sha"][:7]

def latest_build_jenkins(joburl):
	url = joburl.rstrip("/") + "/lastSuccessfulBuild/api/json"
	r = get(url).json()
	return r["number"]

def latest_release_github(joburl):
	url = "https://api.github.com/repos/" + joburl + "/releases/latest"
	r = get(url).json()
	return r["tag_name"]