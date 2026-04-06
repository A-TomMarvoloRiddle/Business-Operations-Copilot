from app.tools.gmail_tools import fetch_emails
from app.tools.calendar_tools import create_event
from app.tools.bigquery_tools import create_task


def get_tools():
    return {
        "fetch_emails": fetch_emails,
        "create_task": create_task,
        "create_event": create_event
    }