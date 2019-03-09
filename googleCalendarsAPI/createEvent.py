from __future__ import print_function
import datetime
import json
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar']

event = {
  #name, describe, and locate the event
  "summary": "ucl api",
  "location": "Malet Place",
  "description": "testing lol alex is a genius",
  "start": {
    #start-date start-time and end time
    "dateTime": "2019-03-09T9:00:00-21:00",
    "timeZone": "Europe/London",
  },
  "end": {
    "dateTime": "2019-03-10T09:00:00-14:00",
    "timeZone": "Europe/London",
  },
  "recurrence": [
    "RRULE:FREQ=DAILY;COUNT=2"
  ],
  "attendees": [
    {"email": "alexisagenius@despacito.com"},
    {"email": "trymebitch@legend.com"},
    {"email": "nathaliealexandra@gmail.com"}
  ],
  "reminders": {
    "useDefault": False,
    "overrides": [
      {"method": "email", "minutes": 24 * 60},
      {"method": "popup", "minutes": 10},
    ],
  },
  #"visibility" : "public"
}

creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
# if os.path.exists('token.pickle'):
#     creds = pickle.loads(open('token.pickle', 'rb').read())
    # with open('token.pickle', 'rb') as token:
    #     creds = pickle.load(token, encoding='iso-8859-1')
        # creds = json.loads(token.read)(
        # u = pickle._Unpickler(token)
        # u.encoding = 'iso-8859-1'
        # p = u.load()
        # print(p)
with open('credentials.json', 'rt') as c:
    creds = json.load(c)
# If there are no (valid) credentials available, let the user log in.
if not creds or 'valid' not in creds:
    if creds and 'expired' in creds and 'refresh_token' in creds:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server()
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)
service = build('calendar', 'v3', credentials=creds)
event = service.events().insert(calendarId='primary', body=event).execute()
print('Event created: ' + (event.get('htmlLink')))
