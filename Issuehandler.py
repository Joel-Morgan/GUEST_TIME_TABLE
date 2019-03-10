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


g = Github("c4dc75d9dda357fc600e27afed237bb071aa87d9")
repo = g.get_repo("Pounder206/GUEST_TIME_TABLE")
repo.create_issue(title, (title + "\n" + siteID + "\n" + roomID + "\n" + start + "\n" + end + "\n" + lecturer))
