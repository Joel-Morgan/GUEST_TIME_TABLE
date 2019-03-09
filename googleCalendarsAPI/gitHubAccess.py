from github import Github
import json

g = Github("27a02591010db73f52dcff492ffce080202ef070")  # personal access token


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
        "reminders": {
            "useDefault": False,
            "overrides": [
                {"method": "email", "minutes": 24 * 60},
                {"method": "popup", "minutes": 10},
            ],
        },
    }
    #x1 = json.dumps(x)
    #loaded = json.loads(x1)
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
        n = makeJSON(issue.title, issue.body.splitLines())
    return n
