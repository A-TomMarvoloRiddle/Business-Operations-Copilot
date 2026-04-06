from google.cloud import bigquery
import uuid
from datetime import datetime

client = bigquery.Client()
DATASET = "business_ops_dataset"

def insert_row(table, data):
    table_id = f"{DATASET}.{table}"
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