from app.tools.bigquery_tools import *

wf = create_workflow("test_user", "Test query")

log_agent("Coordinator", wf, "Planning", "Testing workflow creation")

task_id = create_task(wf, "Test Task", "This is a test task")

print("Workflow:", wf)
print("Task:", task_id)