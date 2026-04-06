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

def fetch_emails(workflow_id, max_results=5):
    service = get_gmail_service()

    results = service.users().messages().list(
        userId='me', maxResults=max_results).execute()

    messages = results.get('messages', [])
    emails = []

    for msg in messages:
        msg_data = service.users().messages().get(
            userId='me', id=msg['id']).execute()

        snippet = msg_data.get('snippet', '')

        emails.append({
            "id": msg['id'],
            "snippet": snippet
        })

    log_tool_call(workflow_id, "gmail_fetch", {}, emails)

    return emails