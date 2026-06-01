# def extract_intent(prompt: str):

#     prompt_lower = prompt.lower()

#     app_type = "custom"

#     app_types = {
#         "crm": "crm",
#         "ecommerce": "ecommerce",
#         "inventory": "inventory",
#         "hr": "hr_tool",
#         "task": "project_management",
#         "project": "project_management",
#         "analytics": "analytics"
#     }

#     for key, value in app_types.items():
#         if key in prompt_lower:
#             app_type = value
#             break

#     feature_keywords = [
#         "login",
#         "dashboard",
#         "payment",
#         "analytics",
#         "chat",
#         "upload",
#         "notifications",
#         "roles"
#     ]

#     features = [
#         feature for feature in feature_keywords
#         if feature in prompt_lower
#     ]

#     integration_keywords = [
#         "slack",
#         "whatsapp",
#         "gmail",
#         "stripe",
#         "jira",
#         "github"
#     ]

#     integrations = [
#         integration for integration in integration_keywords
#         if integration in prompt_lower
#     ]

#     assumptions = []

#     if len(prompt.split()) < 5:
#         assumptions.append(
#             "Prompt is vague, default assumptions applied."
#         )

#     return {
#         "appName": "Generated App",
#         "appType": app_type,
#         "features": features,
#         "entities": [],
#         "integrations_requested": integrations,
#         "assumptions": assumptions
#     }



# import openai
# import json


# def extract_intent(prompt: str):

#     response = openai.chat.completions.create(

#         model="gpt-4o-mini",

#         messages=[

#             {
#                 "role": "system",

#                 "content":
#                 """
#                 Extract app intent as JSON.
#                 Return:
#                 appName,
#                 appType,
#                 features,
#                 integrations_requested,
#                 assumptions
#                 """
#             },

#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ]
#     )

#     content = response.choices[0].message.content

#     try:
#         return json.loads(content)

#     except:

#         return {
#             "appName": "Fallback App",
#             "appType": "custom",
#             "features": [],
#             "entities": [],
#             "integrations_requested": [],
#             "assumptions": [
#                 "Failed to parse AI output"
#             ]
#         }




# import google.generativeai as genai
# from dotenv import load_dotenv
# import os
# import json

# load_dotenv()
# print("KEY:", os.getenv("GEMINI_API_KEY"))
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# model = genai.GenerativeModel("gemini-2.5-flash")

# def extract_intent(prompt):

#     # response = model.generate_content(
#     #     f"""
#     #     Extract app intent from this prompt.

#     #     Return ONLY valid JSON:

#     #     {{
#     #         "appName":"",
#     #         "appType":"",
#     #         "features":[],
#     #         "entities":[],
#     #         "integrations_requested":[],
#     #         "assumptions":[]
#     #     }}
#     #     Return ONLY raw JSON.
#     #     Do not use markdown.
#     #     Do not use ```json.
#     #     Do not add explanations.  
#     #     Prompt:
#     #     {prompt}
#     #     """
#     # )
#     response = model.generate_content(
#         f"""
#         Extract app intent from this prompt.

#         Return ONLY valid JSON:

#        {{
#            "appName": "",
#            "appType": "",
#            "features": [],
#            "entities": [
#            {{
#                 "name": "",
#                 "fields": []
#             }}
#            ],
#            "roles":[],
#            "integrations_requested": [],
#            "assumptions": []
#         }}

#         Rules:
#         - Generate realistic entities for the application.
#         - For each entity generate useful database fields.
#         - Generate realistic user roles for the application.
#         - Include id as a field for every entity.
#         - Return ONLY raw JSON.
#         - Do not use markdown.
#         - Do not use ```json.
#         - Do not add explanations.

#         Prompt:
#         {prompt}
#         """
#     )
#     print(response.text)
#     cleaned = response.text.strip()

#     cleaned = cleaned.replace("```json", "")
#     cleaned = cleaned.replace("```", "")

#     return json.loads(cleaned)












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