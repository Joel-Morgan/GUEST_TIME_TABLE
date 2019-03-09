from github import Github

g = Github("a5a05a98741be468e722d7658e151cb70af0e373")

for repo in g.get_user().get_repos():
    print(repo.name)
  
repo = g.get_repo("Pounder206/GUEST_TIME_TABLE")
open_issues = repo.get_issues(state='open')
for i in open_issues:
  print(i.body)
# title = name of lecture
# body will be lecture name and time  