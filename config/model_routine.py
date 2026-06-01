MODEL_ROUTING = {
    "intent_extraction": {
        "primary": "gpt-4o-mini",
        "fallback": "gemini-flash"
    },

    "schema_generation": {
        "primary": "gpt-4o",
        "fallback": "deepseek"
    },

    "appspec_generation": {
        "primary": "gpt-4o",
        "fallback": "claude-sonnet"
    }
}

# Different AI models do different jobs
# small task  → cheap AI
# big task    → powerful AI
# Intent Extraction :understand prompt
# Schema Generation: Hard work:  generate database + APIs
# Config-driven Meaning: Instead of writing: use gpt-4o everywhere inside code, you store models in ONE config file