from app.tools.bigquery_tools import create_task, save_note, log_agent


def ops_agent(workflow_id, emails):
    log_agent("OpsAgent", workflow_id, "Processing", "Creating tasks from emails")

    task_ids = []

    for email in emails:
        task_id = create_task(
            workflow_id,
            title=f"Follow up: {email['subject']}",
            description=email["snippet"]
        )
        task_ids.append(task_id)

    save_note(
        workflow_id,
        content="Processed emails into tasks",
        summary="Tasks created successfully"
    )

    return task_ids