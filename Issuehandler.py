from github import Github


def inputthings():
    title = input("Title: ")
    siteID = input("SiteID: ")
    roomID = input("Room ID: ")
    start = input("Start Time: ")
    end = input("End Time: ")
    lecturer = input("Lecturer's name: ")
    return title, siteID, roomID, start, end, lecturer


title, siteID, roomID, start, end, lecturer = inputthings()


g = Github("853fe89f989ed7de6ded27f6791f11426114054e")
repo = g.get_repo("Pounder206/GUEST_TIME_TABLE")
repo.create_issue(title, (siteID + "\n" +
                          roomID + "\n" + start + "\n" + end + "\n" + lecturer))
