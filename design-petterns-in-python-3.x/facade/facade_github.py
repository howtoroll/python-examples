import requests


BASE_URL = "https://api.github.com"


# client
def generate_changelog(owner, repo, version):
    github = Facade()
    release_dt = github.get_release_date(owner, repo, version)
    commit_messages = github.get_commit_messages(owner, repo, release_dt)

    changelog = ["CHANGELOG", ""]
    for message in commit_messages:
        changelog.append(f"- {message}")
    return changelog


# facade
class Facade:
    def __init__(self):
        pass

    def get_release_date(self, owner, repo, version):
        url = f"{BASE_URL}/repos/{owner}/{repo}/releases/tags/{version}"
        resp = requests.get(url)
        if resp.status_code == 404:
            raise ValueError("Version does not exist")
        resp.raise_for_status()

        return resp.json()["published_at"]

    def get_commit_messages(self, owner, repo, release_dt):
        url = f"{BASE_URL}/repos/{owner}/{repo}/commits"
        params = {"sha": "master", "since": release_dt}
        resp = requests.get(url, params=params)
        resp.raise_for_status()

        messages = [item.get("commit", {}).get("message") for item in resp.json()]
        return messages[::-1]


# subsystems
# 3rd service API
