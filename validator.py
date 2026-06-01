from integrations.registry import INTEGRATIONS


def validate_appspec(appspec):

    errors = []

    pages = appspec.get("pages", [])
    apis = appspec.get("apiEndpoints", [])

    api_entities = [api["entity"] for api in apis]

    for page in pages:

        if page["entity"] not in api_entities:

            errors.append({
                "type": "PAGE_API_MISMATCH",
                "message": f"No API found for {page['entity']}"
            })

    # Integration Validation

    valid_integrations = [
        item["displayName"]
        for item in INTEGRATIONS
    ]

    for hook in appspec.get("integrationHooks", []):

        if hook["integration"] not in valid_integrations:

            errors.append({
                "type": "INVALID_INTEGRATION",
                "message": f"Unknown integration: {hook['integration']}"
            })
    workflows = appspec.get("workflowStubs", [])

    valid_entities = api_entities

    for workflow in workflows:
        if workflow["triggerEntity"] not in valid_entities:
            errors.append({
                "type": "INVALID_WORKFLOW_ENTITY",
                "message": f"Unknown workflow entity: {workflow['triggerEntity']}"
            })
    if errors:

        return {
            "success": False,
            "errors": errors
        }

    return {
        "success": True,
        "errors": []
    }