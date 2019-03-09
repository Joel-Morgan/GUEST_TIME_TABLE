CREATE EVENT: SETUP
Before you try to run the code or write a similar file remember to set up the directory,
and click "ENABLE THE GOOGLE CALENDAR API" on:
https://developers.google.com/calendar/quickstart/python
BUT make sure to download the credentials.json file within the same directory of the other two files
AND Make sure while you're setting up, you're doing it from the google account you want to create events to and from
then run quickstart.py in python3 in the cmd line (to test your account authorization):
python3 quickstart.py

IMPORTANT: DEPENDENCIES:
make sure you have all the dependencies set up, SPECIFICALLY in python3!!
they are:
github
__future__
datetime
json
pickle
os.path
googleapiclient.discovery
google_auth_oauthlib.flow
google.auth.transport.requests


CREATE EVENT: IN THE CODE
Make sure you're set up properly!! there's a reason this file is called README
To create an event, edit the createEvent file (like it's a json)
The comments explain a bit of it, but mostly it's not counterintuitive
if you have an issue take it up with eatanoctopussy@ucl.ac.uk (or me)

CREATE EVENT: CMD LINE
first (obvi) cd into the right directory
then run the createEvent in python 3 (this should authorize you to create events to that account's google calendar):
python3 createEvent.py
then add the event:
event()
it'll prompt a function; please type:
createEvent.py

CREATE EVENT: THANK CHRIS
most importantly hug chris for figuring out our encoding issues

THAT'S IT don't fuck up :)
xx- Alex for the Google Calendars API end and Rikaz for the GitHub API end
