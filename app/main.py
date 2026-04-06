import json
from vertexai.preview.generative_models import GenerativeModel
from app.tools.agent_tools import get_tools
from app.tools.bigquery_tools import create_workflow, log_agent
from app.prompts.system_prompts import COORDINATOR_PROMPT, VERIFIER_PROMPT

model = GenerativeModel("gemini-2.5-flash")


def run_agent(user_id, query):

    workflow_id = create_workflow(user_id, query)
    tools = get_tools()

    # Planning
    planning_prompt = f"""{COORDINATOR_PROMPT} User request: {query} """

    log_agent("Coordinator", workflow_id, "Planning", query)

    response = model.generate_content(planning_prompt)
    text = response.text.strip()

    try:
        plan = json.loads(text)["plan"]
    except Exception:
        return {
            "workflow_id": workflow_id,
            "error": "Planner failed",
            "raw_output": text
        }

    # Execution
    results = []

    for step in plan:
        action = step.get("action")
        args = step.get("args", {})

        log_agent("Executor", workflow_id, f"Executing {action}", str(args))

        if action in tools:
            try:
                result = tools[action](workflow_id, **args)

                results.append({
                    "action": action,
                    "status": "success",
                    "output": str(result)
                })

            except Exception as e:
                results.append({
                    "action": action,
                    "status": "failed",
                    "error": str(e)
                })
        else:
            results.append({
                "action": action,
                "status": "unknown_tool"
            })

    #Verification
    verifier_prompt = f"""{VERIFIER_PROMPT} User request: {query} Execution results: {json.dumps(results, indent=2)}"""

    log_agent("Verifier", workflow_id, "Verifying", "Checking execution results")

    verifier_response = model.generate_content(verifier_prompt)
    verifier_text = verifier_response.text.strip()

    try:
        verification = json.loads(verifier_text)
    except Exception:
        return {
            "workflow_id": workflow_id,
            "error": "Verifier failed",
            "raw_output": verifier_text,
            "execution_results": results
        }

    #Reflection/Retry
    retry_results = []

    if verification.get("status") == "FAILED":
        for retry in verification.get("retry_actions", []):
            action = retry.get("action")
            args = retry.get("args", {})

            log_agent("Reflection", workflow_id, f"Retrying {action}", str(args))

            if action in tools:
                try:
                    result = tools[action](workflow_id, **args)

                    retry_results.append({
                        "action": action,
                        "status": "retried_success",
                        "output": str(result)
                    })

                except Exception as e:
                    retry_results.append({
                        "action": action,
                        "status": "retried_failed",
                        "error": str(e)
                    })
            else:
                retry_results.append({
                    "action": action,
                    "status": "unknown_tool"
                })

    #Final
    return {
        "workflow_id": workflow_id,
        "plan": plan,
        "execution_results": results,
        "verification": verification,
        "retry_results": retry_results
    }