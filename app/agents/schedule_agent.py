from app.tools.calendar_tools import create_event
from app.tools.bigquery_tools import log_agent
from datetime import datetime, timedelta


def schedule_agent(workflow_id):
    log_agent("ScheduleAgent", workflow_id, "Scheduling", "Creating a meeting")

    start = datetime.utcnow().isoformat()
    end = (datetime.utcnow() + timedelta(hours=1)).isoformat()

    event_id = create_event(
        workflow_id,
        "Follow-up Meeting",
        start,
        end
    )

    return event_id