from app.tools.gmail_tools import fetch_emails
from app.tools.bigquery_tools import log_agent


def inbox_agent(workflow_id):
    log_agent("InboxAgent", workflow_id, "Fetching Emails", "Retrieving latest emails")

    emails = fetch_emails(workflow_id)

    return emails