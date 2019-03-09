import github3
github = github3.login(token = "a5a05a98741be468e722d7658e151cb70af0e373")
issues = github.issue("Pounder206", "Pounder206/GUEST_TIME_TABLE", "1")
print(issues)
