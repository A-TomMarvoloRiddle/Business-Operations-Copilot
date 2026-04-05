-- USERS
CREATE TABLE Hack_C1_dataset.users (
  user_id STRING,
  email STRING,
  created_at TIMESTAMP
);

-- WORKFLOW RUNS
CREATE TABLE Hack_C1_dataset.workflow_runs (
  workflow_id STRING,
  user_id STRING,
  query STRING,
  status STRING,
  created_at TIMESTAMP,
  completed_at TIMESTAMP
);

-- EMAILS
CREATE TABLE Hack_C1_dataset.emails (
  email_id STRING,
  workflow_id STRING,
  subject STRING,
  sender STRING,
  summary STRING,
  raw_snippet STRING,
  created_at TIMESTAMP
);

-- TASKS
CREATE TABLE Hack_C1_dataset.tasks (
  task_id STRING,
  workflow_id STRING,
  title STRING,
  description STRING,
  priority STRING,
  status STRING,
  due_date TIMESTAMP,
  created_at TIMESTAMP
);

-- CALENDAR EVENTS
CREATE TABLE Hack_C1_dataset.calendar_events (
  event_id STRING,
  workflow_id STRING,
  title STRING,
  start_time TIMESTAMP,
  end_time TIMESTAMP,
  attendees STRING,
  status STRING,
  created_at TIMESTAMP
);

-- NOTES
CREATE TABLE Hack_C1_dataset.notes (
  note_id STRING,
  workflow_id STRING,
  content STRING,
  summary STRING,
  created_at TIMESTAMP
);

-- AGENT LOGS
CREATE TABLE Hack_C1_dataset.agent_logs (
  log_id STRING,
  workflow_id STRING,
  agent_name STRING,
  action STRING,
  reasoning STRING,
  timestamp TIMESTAMP
);

-- TOOL CALLS
CREATE TABLE Hack_C1_dataset.tool_calls (
  call_id STRING,
  workflow_id STRING,
  tool_name STRING,
  input STRING,
  output STRING,
  status STRING,
  timestamp TIMESTAMP
);