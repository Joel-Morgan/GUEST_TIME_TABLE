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


g = Github("6a1ea1fb97adc7b0a4f9cd66d9118dec4cdb98f0")
repo = g.get_repo("Pounder206/GUEST_TIME_TABLE")
repo.create_issue(title, (siteID + "\n" +
                          roomID + "\n" + start + "\n" + end + "\n" + lecturer))
