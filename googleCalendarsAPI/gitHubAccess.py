from base64 import b64decode

from github import Github
import json

g = Github("472a461fe503c6eb64bd4a3fb9bb0b92c2a5d1e1")  # personal access token


def makeJSON(title, body):
    x = {
        "summary": title,
        "location": body[0],
        "start": {
            "dateTime": body[1],
            "timeZone": "Europe/London",
        },
        "end": {
            "dateTime": body[2],
            "timeZone": "Europe/London",
        },
        "attendees": body[3],
    }
    # x1 = json.dumps(x)
    # loaded = json.loads(x1)
    print(x)
    return x


def getIssues():
    # gets joel's repo and assigns to repo
    for repo in g.get_user().get_repos():
        if repo.name == "GUEST_TIME_TABLE":
            break

    # gets all the issues that are open on the repo
    issueList = repo.get_issues(state="open")
    # for each issue create a json
    for issue in issueList:
        title = issue.title
        file = repo.get_contents(title + ".json")
        # print(file.content)
        decoded = b64decode(file.content)
        load = json.loads(decoded)
        body = [load["address"], load["start"], load["end"], load["lecturer"]]
        n = makeJSON(title, body)
    return n


getIssues()
