
def generate_schema(app_intent):

    entities = []

    extracted_entities = app_intent.get("entities", [])

    if extracted_entities:

        for entity in extracted_entities:

            entities.append(
                {
                    "name": entity["name"],
                    "tableName": entity["name"].lower().replace(" ", "_") + "s",
                    "fields": entity["fields"]
                }
            )

    else:

        entities = [
            {
                "name": "CustomEntity",
                "tableName": "custom_entities",
                "fields": [
                    {
                        "name": "id",
                        "type": "UUID"
                    }
                ]
            }
        ]

    return {
        "entities": entities
    }