from app.agents.coordinator import run_workflow

result = run_workflow(
    user_id="test_user",
    query="Process my emails and schedule follow-up"
)

print(result)