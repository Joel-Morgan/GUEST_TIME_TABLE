from base64 import b64decode

from github import Github
import json

g = Github("115803c9cc7e7697ba798fb5f618d353a09e99aa")  # personal access token


def makeJSON(title, body):
  # 20191109T010000     2019-11-09T01:00:00

    x = {
        "summary": title,
        "location": body[0],
        "start": {
            "dateTime": formatTime(body[1]),
            "timeZone": "Europe/London",
        },
        "end": {
            "dateTime": formatTime(body[2]),
            "timeZone": "Europe/London",
        },
        "attendees": body[3],
    }
    # x1 = json.dumps(x)
    # loaded = json.loads(x1)
    print(x)
    return x


def formatTime(dateTime):
    year = dateTime[:4]
    month = dateTime[4] + dateTime[5]
    day = dateTime[6] + dateTime[7]
    time = dateTime[9] + dateTime[10] + ":" + dateTime[11] + \
        dateTime[12] + ":" + dateTime[13] + dateTime[14]
    formatted = year + "-" + month + "-" + day + "T" + time
    return formatted


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
