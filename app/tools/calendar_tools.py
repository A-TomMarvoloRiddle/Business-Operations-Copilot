from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import pickle
from google.oauth2.credentials import Credentials
from datetime import datetime, timedelta

from app.tools.bigquery_tools import log_tool_call, create_calendar_event

SCOPES = ['https://www.googleapis.com/auth/calendar']


def get_calendar_service():
    creds = None

    if os.path.exists("token_calendar.json"):
       creds = Credentials.from_authorized_user_file("token_calendar.json", SCOPES)

    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=8080)

        with open("token_calendar.json", "w") as token:
            token.write(creds.to_json())

    return build('calendar', 'v3', credentials=creds)

def create_event(workflow_id, summary, start_time, end_time):
    service = get_calendar_service()

    event = {
        'summary': summary,
        'start': {'dateTime': start_time, 'timeZone': 'UTC'},
        'end': {'dateTime': end_time, 'timeZone': 'UTC'},
    }

    created_event = service.events().insert(
        calendarId='primary', body=event).execute()

    create_calendar_event(
        workflow_id=workflow_id,
        title=summary,
        start_time=start_time,
        end_time=end_time,
        attendees="self"
    )

    log_tool_call(workflow_id, "calendar_create", event, created_event)

    return created_event['id']