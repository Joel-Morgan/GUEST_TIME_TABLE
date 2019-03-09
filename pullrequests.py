import requests

params = {
  "token": "uclapi-0eac141bbe42a7c-0e904afa5d2cd9e-37b791f7306b99b-2d94e443381db8e"
}
r = requests.get("https://uclapi.com/roombookings/rooms", params=params).
print(r.json())

