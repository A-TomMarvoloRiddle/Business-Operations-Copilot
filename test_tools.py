from app.tools.gmail_tools import fetch_emails
from app.tools.calendar_tools import create_event
from app.tools.bigquery_tools import create_workflow

from datetime import datetime, timedelta, timezone

wf = create_workflow("test_user", "Final Fixed Testing Gmail + Calendar Tools")

emails = fetch_emails(wf)
#print("Emails:", emails)

start = datetime.now(timezone.utc).isoformat()
end = (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat()

event_id = create_event(wf, "Final Test Meeting", start, end)
#print("Event ID:", event_id)