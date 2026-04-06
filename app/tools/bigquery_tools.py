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
