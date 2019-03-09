from github import Github

g = Github("698ea9b37150a93463c3f2834021a20a8bb84654")

#for repo in g.get_user().get_repos():
#    print(repo.name)
  
repo = g.get_repo("Pounder206/GUEST_TIME_TABLE")
open_issues = repo.get_issues(state='open')
for i in open_issues:
  print(i.title)
  print((i.body).split())
# title = name of lecture
# body will be lecture name and time  