from app.tools.bigquery_tools import create_workflow, log_agent
from app.agents.inbox_agent import inbox_agent
from app.agents.schedule_agent import schedule_agent
from app.agents.ops_agent import ops_agent
from app.agents.verifier_agent import verifier_agent


def run_workflow(user_id, query):
    workflow_id = create_workflow(user_id, query)

    log_agent("Coordinator", workflow_id, "Planning", "Starting workflow")

    # Step 1: Inbox
    emails = inbox_agent(workflow_id)

    # Step 2: Ops
    tasks = ops_agent(workflow_id, emails)

    # Step 3: Schedule
    event = schedule_agent(workflow_id)

    # Step 4: Verify
    status = verifier_agent(workflow_id, tasks and event)

    return {
        "workflow_id": workflow_id,
        "emails_processed": len(emails),
        "tasks_created": len(tasks),
        "event_created": event,
        "status": status
    }