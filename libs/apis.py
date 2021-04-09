from requests import get

def latest_commit_github(repo, branch):
	url = "https://api.github.com/repos/" + repo + "/commits/" + branch
	r = get(url).json()
	return r["sha"][:7]