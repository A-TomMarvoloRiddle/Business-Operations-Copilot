import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

from app.tools.bigquery_tools import log_tool_call, save_email

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def get_gmail_service():
    creds = None

    # Load existing token
    if os.path.exists("token_gmail.json"):
       creds = Credentials.from_authorized_user_file("token_gmail.json", SCOPES)

    # If no valid creds -> authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            
            creds = flow.run_local_server(port=8080)

        # Save token
        with open("token_gmail.json", "w") as token:
            token.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)


def fetch_emails(workflow_id, max_results=5):
    service = get_gmail_service()

    results = service.users().messages().list(
        userId="me", maxResults=max_results
    ).execute()

    messages = results.get("messages", [])
    emails = []

    for msg in messages:
        msg_data = service.users().messages().get(
            userId="me", id=msg["id"]
        ).execute()

        snippet = msg_data.get("snippet", "")

        headers = msg_data.get("payload", {}).get("headers", [])

        subject = "N/A"
        sender = "N/A"

        for h in headers:
            if h["name"] == "Subject":
                subject = h["value"]
            elif h["name"] == "From":
                sender = h["value"]

        email_obj = {
            "id": msg["id"],
            "subject": subject,
            "sender": sender,
            "snippet": snippet
        }

        emails.append(email_obj)

        save_email(
            workflow_id=workflow_id,
            subject=subject,
            sender=sender,
            summary=snippet,
            raw_snippet=snippet
        )

    log_tool_call(workflow_id, "gmail_fetch", {}, emails)

    return emails