from github import Github

g = Github("4b1fd50ddd571e8bba0ec82937ff5b61f939f3d7")

for repo in g.get_user().get_repos():
    print(repo.name)
  
repo = g.get_user().get_repos("GUEST_TIME_TABLE")

open_issues = repo.get_issues(state='open')
for issue in open_issues:
  print(issues)
# title = name of lecture
# body will be lecture name and time  