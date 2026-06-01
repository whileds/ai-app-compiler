INTEGRATIONS = [

    {
        "id": "slack",
        "displayName": "Slack",
        "authType": "oauth2",

        "actions": [
            "send_message",
            "send_dm"
        ]
    },

    {
        "id": "whatsapp",
        "displayName": "WhatsApp",
        "authType": "api_key",

        "actions": [
            "send_template_message"
        ]
    },

    {
        "id": "gmail",
        "displayName": "Gmail",
        "authType": "oauth2",

        "actions": [
            "send_email"
        ]
    },

    {
        "id": "stripe",
        "displayName": "Stripe",
        "authType": "api_key",

        "actions": [
            "create_payment"
        ]
    },

    {
        "id": "jira",
        "displayName": "Jira",
        "authType": "oauth2",

        "actions": [
            "create_issue"
        ]
    }
]