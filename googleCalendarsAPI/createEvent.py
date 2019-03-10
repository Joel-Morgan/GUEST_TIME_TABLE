from __future__ import print_function
import datetime
import json
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import gitHubAccess

SCOPES = ['https://www.googleapis.com/auth/calendar']
# this commented section is how to create an event without going through gitHub
# use it if you want to hard code the event i guess
'''event = {
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
}'''
event = gitHubAccess.getIssues()
creds = None
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
