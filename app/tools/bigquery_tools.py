from google.cloud import bigquery
import uuid
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
DATASET = os.getenv("DATASET")

client = bigquery.Client()


def insert_row(table, data):
    table_id = f"{PROJECT_ID}.{DATASET}.{table}"
    errors = client.insert_rows_json(table_id, [data])

    if errors:
        raise Exception(f"BigQuery Insert Error: {errors}")

def create_workflow(user_id, query):
    workflow_id = str(uuid.uuid4())

    data = {
        "workflow_id": workflow_id,
        "user_id": user_id,
        "query": query,
        "status": "pending",
        "created_at": datetime.utcnow().isoformat(),
        "completed_at": None
    }

    insert_row("workflow_runs", data)

    return workflow_id

def log_agent(agent_name, workflow_id, action, reasoning):
    data = {
        "log_id": str(uuid.uuid4()),
        "workflow_id": workflow_id,
        "agent_name": agent_name,
        "action": action,
        "reasoning": reasoning,
        "timestamp": datetime.utcnow().isoformat()
    }

    insert_row("agent_logs", data)

def log_tool_call(workflow_id, tool_name, input_data, output_data, status="success"):
    data = {
        "call_id": str(uuid.uuid4()),
        "workflow_id": workflow_id,
        "tool_name": tool_name,
        "input": str(input_data),
        "output": str(output_data),
        "status": status,
        "timestamp": datetime.utcnow().isoformat()
    }

    insert_row("tool_calls", data)

def create_task(workflow_id, title, description, priority="medium"):
    task_id = str(uuid.uuid4())

    data = {
        "task_id": task_id,
        "workflow_id": workflow_id,
        "title": title,
        "description": description,
        "priority": priority,
        "status": "pending",
        "due_date": None,
        "created_at": datetime.utcnow().isoformat()
    }

    insert_row("tasks", data)

    return task_id

def save_email(workflow_id, subject, sender, summary, raw_snippet):
    email_id = str(uuid.uuid4())

    data = {
        "email_id": email_id,
        "workflow_id": workflow_id,
        "subject": subject,
        "sender": sender,
        "summary": summary,
        "raw_snippet": raw_snippet,
        "created_at": datetime.utcnow().isoformat()
    }

    insert_row("emails", data)

    return email_id

def create_calendar_event(workflow_id, title, start_time, end_time, attendees):
    event_id = str(uuid.uuid4())

    data = {
        "event_id": event_id,
        "workflow_id": workflow_id,
        "title": title,
        "start_time": start_time,
        "end_time": end_time,
        "attendees": attendees,
        "status": "scheduled",
        "created_at": datetime.utcnow().isoformat()
    }

    insert_row("calendar_events", data)

    return event_id

def save_note(workflow_id, content, summary):
    note_id = str(uuid.uuid4())

    data = {
        "note_id": note_id,
        "workflow_id": workflow_id,
        "content": content,
        "summary": summary,
        "created_at": datetime.utcnow().isoformat()
    }

    insert_row("notes", data)

    return note_id