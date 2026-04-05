-- USERS
CREATE TABLE users (
  user_id STRING,
  email STRING,
  created_at TIMESTAMP
);

-- WORKFLOW RUNS (core table)
CREATE TABLE workflow_runs (
  workflow_id STRING,
  user_id STRING,
  query STRING,
  status STRING, -- pending / success / failed
  created_at TIMESTAMP,
  completed_at TIMESTAMP
);

-- EMAILS
CREATE TABLE emails (
  email_id STRING,
  workflow_id STRING,
  subject STRING,
  sender STRING,
  summary STRING,
  raw_snippet STRING,
  created_at TIMESTAMP
);

-- TASKS
CREATE TABLE tasks (
  task_id STRING,
  workflow_id STRING,
  title STRING,
  description STRING,
  priority STRING,
  status STRING, -- pending / done
  due_date TIMESTAMP,
  created_at TIMESTAMP
);

-- CALENDAR EVENTS
CREATE TABLE calendar_events (
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
CREATE TABLE notes (
  note_id STRING,
  workflow_id STRING,
  content STRING,
  summary STRING,
  created_at TIMESTAMP
);

-- AGENT LOGS (very important for judging)
CREATE TABLE agent_logs (
  log_id STRING,
  workflow_id STRING,
  agent_name STRING,
  action STRING,
  reasoning STRING,
  timestamp TIMESTAMP
);

-- TOOL CALLS (MCP tracking)
CREATE TABLE tool_calls (
  call_id STRING,
  workflow_id STRING,
  tool_name STRING,
  input STRING,
  output STRING,
  status STRING,
  timestamp TIMESTAMP
);