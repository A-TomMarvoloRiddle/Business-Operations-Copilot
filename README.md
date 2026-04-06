# Business Ops Copilot — Multi-Agent AI Execution System

> **An AI system that doesn’t just suggest work — it executes, verifies, and logs it.**

---

## 🧠 Overview

**Business Ops Copilot** is a multi-agent AI system that transforms unstructured communication (emails, notes, requests) into **executed workflows** across real-world tools like Gmail and Google Calendar.

Unlike traditional assistants, this system:

* Plans actions using LLMs
* Executes them via tool integrations
* Verifies outcomes
* Stores everything in a structured, queryable system (BigQuery)

---

## 🧩 Key Features

### 🧠 Multi-Agent Architecture

* **Coordinator Agent** → Plans workflow using LLM
* **Executor Layer** → Executes tool actions
* **Verifier Agent** → Validates outcomes & triggers retries

---

### 🔄 Planner–Executor–Verifier Loop

```text
User → Planner → Execution → Verification → Retry (if needed)
```

---

### 🔌 Real Tool Integrations

* Gmail API → Fetch & process emails
* Google Calendar API → Schedule events
* BigQuery → Structured storage & audit logs

---

### 🗃️ Structured Memory (BigQuery)

All system activity is stored as structured data:

* emails
* tasks
* calendar events
* workflow runs
* agent logs
* tool calls

---

### 🔍 Observability & Auditability

Every action is logged:

* Which agent acted
* What decision was made
* Which tool was called
* What result was produced

---

### 🔁 Self-Correcting System

* Detects failures
* Retries actions
* Ensures reliability

---

## 🏗️ Architecture

```text
                ┌──────────────┐
                │   User Input │
                └──────┬───────┘
                       │
               ┌───────▼────────┐
               │  Coordinator   │ (LLM Planner)
               └───────┬────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
┌───────▼───────┐ ┌────▼─────┐ ┌──────▼──────┐
│ Inbox Agent   │ │ Ops Agent│ │ Schedule    │
│ (Gmail)       │ │ (Tasks)  │ │ Agent       │
└───────┬───────┘ └────┬─────┘ └──────┬──────┘
        │              │              │
        └──────────────┼──────────────┘
                       │
               ┌───────▼────────┐
               │   BigQuery     │ (Memory)
               └───────┬────────┘
                       │
               ┌───────▼────────┐
               │  Verifier      │ (LLM)
               └────────────────┘
```

---

## ⚙️ Tech Stack

| Layer           | Technology              |
| --------------- | ----------------------- |
| LLM             | Gemini (Vertex AI)      |
| Agent Framework | Google ADK              |
| Database        | BigQuery                |
| APIs            | Gmail API, Calendar API |
| Language        | Python                  |
| Auth            | OAuth 2.0               |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd business-ops-copilot
```

---

### 2. Setup environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

### 3. Configure environment variables

Create `.env`:

```env
PROJECT_ID=your-project-id
DATASET=business_ops_dataset
```

---

### 4. Setup Google Cloud

* Enable:

  * BigQuery API
  * Gmail API
  * Calendar API
  * Vertex AI API

---

### 5. Setup OAuth

* Create OAuth Client (Desktop App)
* Download `credentials.json`
* Place in root directory

---

### 6. Create BigQuery tables

```bash
bq mk business_ops_dataset
bq query --use_legacy_sql=false < app/schemas/bigquery_schema.sql
```

---

### 7. Run the system

```bash
python test_llm.py
```

---

## 🧪 Example Usage

```python
from app.main import run_agent

result = run_agent(
    "user_1",
    "Check my emails, create tasks, and schedule a meeting"
)

print(result)
```

---

## 📊 Example Output

```json
{
  "workflow_id": "...",
  "plan": [
    {"action": "fetch_emails"},
    {"action": "create_task"},
    {"action": "create_event"}
  ],
  "execution_results": [...],
  "verification": {
    "status": "SUCCESS"
  }
}
```

---

## 🔍 BigQuery Tables

| Table           | Description            |
| --------------- | ---------------------- |
| workflow_runs   | Tracks each request    |
| emails          | Stored email summaries |
| tasks           | Generated tasks        |
| calendar_events | Scheduled meetings     |
| agent_logs      | Agent reasoning        |
| tool_calls      | Tool execution logs    |

---

## 🏆 What Makes This Unique

* Not a chatbot → **execution system**
* Multi-agent architecture
* Real API integrations
* Structured memory (BigQuery)
* Self-verifying workflows
* Production-style observability

---

## 🔮 Future Improvements

* Slack / Notion integration
* Real-time triggers (webhooks)
* Priority classification using ML
* Conflict-aware scheduling
* Autonomous workflows

---

## 👤 Author

**Apaar Mathur**
AI Engineer | Multi-Agent Systems | Applied AI

---

> ⚡ *“From assistants that suggest → to systems that execute.”*
