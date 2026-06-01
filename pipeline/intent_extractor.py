
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

load_dotenv()
print("KEY:", os.getenv("GEMINI_API_KEY"))
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def extract_intent(prompt):

    try:

        response = model.generate_content(
            f"""
            Extract app intent from this prompt.

            Return ONLY valid JSON:

            {{
                "appName": "",
                "appType": "",
                "features": [],
                "entities": [
                    {{
                        "name": "",
                          "fields": [
                            {{
                              "name": "",
                              "type": "",
                              "nullable": null,
                              "unique": null,
                              "references": null,
                              "values": []
                            }}
                          ]
                    }}
                ],
                "roles": [],
                "integrations_requested": [],
                "assumptions": []
            }}

            Rules:
            - Generate realistic entities for the application.
            - Generate useful database fields for each entity.
            - Include id as a field for every entity.
            - Generate realistic user roles for the application.
            - Return ONLY raw JSON.
            - Do not use markdown.
            - Do not use ```json.
            - Do not add explanations.
            - Infer realistic database types.
            - Use UUID for primary keys.
            - Detect foreign keys and populate references.
            - For status/category fields use Enum.
            - Populate enum values.
            - Set nullable appropriately.
            - Set unique appropriately.
            - Return fields as objects, not strings.
            - Foreign key fields should use:
  {{
    "name":"patient_id",
    "type":"Foreign Key",
    "references":"Patient"
  }}
            - Enum fields should include values array.                        
Example:

{{
  "name": "status",
  "type": "Enum",
  "values": [
    "Active",
    "Inactive"
  ]
}}
            Prompt:
            {prompt}
            """
        )

        print(response.text)

        cleaned = response.text.strip()
        cleaned = cleaned.replace("```json", "")
        cleaned = cleaned.replace("```", "")

        return json.loads(cleaned)

    except Exception as e:

        print("Gemini Error:", e)

        return {
            "appName": "Unknown",
            "appType": "Unknown",
            "features": [],
            "entities": [],
            "roles": ["admin"],
            "integrations_requested": [],
            "assumptions": [],
            "error": str(e)
        }