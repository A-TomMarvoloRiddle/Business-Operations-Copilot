from app.tools.bigquery_tools import log_agent


def verifier_agent(workflow_id, result):
    log_agent(
        "VerifierAgent",
        workflow_id,
        "Verification",
        "Checking if workflow completed"
    )

    if result:
        return "SUCCESS"
    return "FAILED"