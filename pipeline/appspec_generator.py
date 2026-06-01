def generate_appspec(data_schema,app_intent):

    entities = data_schema.get("entities", [])

    pages = []
    api_endpoints = []

    for entity in entities:

        entity_name = entity["name"]

        pages.append({
            "name": f"{entity_name} List",
            "route": f"/{entity_name.lower()}",
            "layout": "list",
            "entity": entity_name
        })

        # api_endpoints.append({
        #     "path": f"/api/{entity_name.lower()}",
        #     "method": "GET",
        #     "entity": entity_name,
        #     "authRequired": True
        # })
        api_endpoints.extend([
            {
                "path": f"/api/{entity_name.lower()}",
                "method": "GET",
                "entity": entity_name,
                "authRequired": True
            },

            {
                "path": f"/api/{entity_name.lower()}",
                "method": "POST",
                "entity": entity_name,
                "authRequired": True
            },

            {
                "path": f"/api/{entity_name.lower()}/{{id}}",
                "method": "PUT",
                "entity": entity_name,
                "authRequired": True
            },

            {
                "path": f"/api/{entity_name.lower()}/{{id}}",
                "method": "DELETE",
                "entity": entity_name,
                "authRequired": True
            }

        ])

    integration_hooks = []
    workflow_stubs = []

    integrations = data_schema.get(
        "integrations_requested",
        []
    )

    for integration in integrations:
        action = "send_message"

        if integration.lower() == "gmail":
            action = "send_email"

        elif integration.lower() == "stripe":
            action = "create_payment"

        elif integration.lower() == "jira":
            action = "create_issue"

        elif integration.lower() == "whatsapp":
            action = "send_template_message"

        elif integration.lower() == "slack":
            action = "send_message"
        else:
            action = "default_action"

        integration_hooks.append({

            "integration": integration,

            "action": action
        })

        workflow_stubs.append({

            "name": f"{integration} workflow",
            
            "triggerEntity": entities[0]["name"] if entities else "Unknown",

            "integration": integration,

            "action": action
        })

       

    return {

        "pages": pages,

        "apiEndpoints": api_endpoints,

        "authRules": {
            "roles": data_schema.get("roles",["admin", "user"])
        },

        "integrationHooks": integration_hooks,

        "workflowStubs": workflow_stubs
    }