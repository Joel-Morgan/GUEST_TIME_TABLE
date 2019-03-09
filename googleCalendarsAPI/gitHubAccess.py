from github import Github
import json

g = Github("b4a6b378d632fe1319210f2540d16c5122f6c193")  # personal access token


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
    # x1 = json.dumps(x)
    # loaded = json.loads(x1)
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
        print(file.content)
        load = json.loads(file.content)
        body = [load["address"], load["start"], load["end"], load["lecturer"]]
        n = makeJSON(title, body)
    return n


getIssues()
