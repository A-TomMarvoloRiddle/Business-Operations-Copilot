from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import pickle

from app.tools.bigquery_tools import log_tool_call

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def get_gmail_service():
    creds = None

    if os.path.exists('token.pkl'):
        with open('token.pkl', 'rb') as token:
            creds = pickle.load(token)

    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

        with open('token.pkl', 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)