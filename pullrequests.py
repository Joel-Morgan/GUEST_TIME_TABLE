from github import Github
import requests
import json

g = Github("ae8f59ab1eada6109faaff5e5075ec1adf07b6bf")
  
repo = g.get_repo("Pounder206/GUEST_TIME_TABLE")
open_issues = repo.get_issues(state='open')
for i in open_issues:
  roomDetails = []
  roomDetails.append(i.title)
  temporary = i.body.split()
  for j in temporary:
    roomDetails.append(j)
  print(roomDetails)
  params = {
  "token": "uclapi-0eac141bbe42a7c-0e904afa5d2cd9e-37b791f7306b99b-2d94e443381db8e",
  "roomid": roomDetails[1],
  "siteid": roomDetails[2]
  }
  r = requests.get("https://uclapi.com/roombookings/rooms", params=params)
  roomLocation = r.json()['rooms'][0]['location']['address']
  roomLocation = " ".join(roomLocation)
  print(roomLocation)
  fileLocation = roomDetails[0] + ".json"
  
  #data = "\"title\":" + roomdet
  data = {
    "title" : roomDetails[0],
    "address" : roomLocation,
    "start" : roomDetails[3],
    "end": roomDetails[4],
    "lecturer": roomDetails[5]
  }

  """data = "{" +
  "\"title\":" + roomDetails[0] + ","
  "\"address\":" + roomLocation + ","
  "\"start\":" + roomDetails[3] + ","
  "\"end\":" + roomDetails[4] + ","
  "\"lecturer\":" + roomDetails[5] + "}"""


  with open(fileLocation, 'w') as outfile:  
    json.dump(data, outfile)
  repo.create_file(str(roomDetails[0]) + ".json" , "ImagineThisWorkingLOL", json.dumps(data))

# title = name of lecture
# body will be lecture name and time  
# room details 0 = title 
# roomdetails 1 = room ID
# room details 2 = site ID
# room details 3 = start time
# room details 4 = end time
# room detials 5 = lecturer 

