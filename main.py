



from fastapi import FastAPI
from pydantic import BaseModel

from pipeline.intent_extractor import extract_intent
from pipeline.schema_generator import generate_schema
from pipeline.appspec_generator import generate_appspec
from integrations.registry import INTEGRATIONS
from validator import validate_appspec
from repair_engine import repair_appspec
from config.cost_config import COST_TABLE
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from sse_starlette.sse import EventSourceResponse
# import json
import json
# import time
import asyncio
import time
app = FastAPI()
app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str

# @app.get("/api/generate-stream")
# async def generate_stream():
    
#     # await asyncio.sleep(1)

#     async def event_generator():

#         yield {
#             "event": "message",
#             "data": "Intent Extraction Started"
#         }
#         await asyncio.sleep(1)
#         yield {
#             "event": "message",
#             "data": "Intent Extraction Completed"
#         }
#         await asyncio.sleep(1)

#         yield {
#             "event": "message",
#             "data": "Schema Generation Started"
#         }
#         await asyncio.sleep(1)

#         yield {
#             "event": "message",
#             "data": "Schema Generation Completed"
#         }
#         await asyncio.sleep(1)

#         yield {
#             "event": "message",
#             "data": "AppSpec Generation Started"
#         }
#         await asyncio.sleep(1)

#         yield {
#             "event": "message",
#             "data": "AppSpec Generation Completed"
#         }
#         await asyncio.sleep(1)

#         yield {
#             "event": "message",
#             "data": "Validation Passed"
#         }

#     # return StreamingResponse(
#     #     event_generator(),
#     #     media_type="text/event-stream"
#     # )
#     return EventSourceResponse(event_generator())
@app.post("/api/generate-stream")
async def generate_stream(request: PromptRequest):

    async def event_generator():

        try:

            yield {
                "event": "message",
                "data": "Intent Extraction Started"
            }

            intent = extract_intent(request.prompt)

            yield {
                "event": "message",
                "data": "Intent Extraction Completed"
            }

            if "error" in intent:

                yield {
                    "event": "error",
                    "data": intent["error"]
                }

                return

            yield {
                "event": "message",
                "data": "Schema Generation Started"
            }

            schema = generate_schema(intent)

            yield {
                "event": "message",
                "data": "Schema Generation Completed"
            }

            yield {
                "event": "message",
                "data": "AppSpec Generation Started"
            }

            appspec = generate_appspec(
                {
                    **schema,
                    "integrations_requested":
                        intent["integrations_requested"],
                    "roles":
                        intent.get("roles", ["admin"])
                },
                intent
            )

            yield {
                "event": "message",
                "data": "AppSpec Generation Completed"
            }

            yield {
                "event": "message",
                "data": "Validation Started"
            }

            validation = validate_appspec(appspec)

            yield {
                "event": "message",
                "data": "Validation Completed"
            }

            result = {
                "intent": intent,
                "schema": schema,
                "appspec": appspec,
                "validation": validation
            }

            yield {
                "event": "result",
                "data": json.dumps(result)
            }

            yield {
                "event": "complete",
                "data": "DONE"
            }

        except Exception as e:

            yield {
                "event": "error",
                "data": str(e)
            }

    return EventSourceResponse(event_generator())
@app.get("/")
def home():
    return {
        "message": "OneAtlas AI Pipeline Running"
    }

@app.get("/api/integrations")
def get_integrations():

    return {
        "integrations": INTEGRATIONS
    }

@app.post("/api/generate")
def generate_app(request: PromptRequest):
    start_time = time.time()
    trace_log = []

    trace_log.append(
        "Intent Extraction Started"
    )
    # Stage 1
    intent = extract_intent(request.prompt)
    trace_log.append("Intent Extraction Completed")

    trace_log.append("Schema Generation Started")
    print(intent)
    if "error" in intent:
        return {
            "success": False,
            "error": intent["error"]
        }
    intent_time = time.time()
    # Stage 2
    schema = generate_schema(intent)
    trace_log.append("Schema Generation Completed")

    trace_log.append("AppSpec Generation Started")
    schema_time = time.time()
    # Stage 3
    appspec = generate_appspec({
        **schema,
        "integrations_requested":
            intent["integrations_requested"],
        "roles":
            intent.get("roles", ["admin"])    
    },intent)
    trace_log.append("AppSpec Generation Completed")

    trace_log.append("Validation Started")
    appspec_time = time.time()
    # Validation
    validation = validate_appspec(appspec)
    trace_log.append("Validation Completed")
    repair_log = []

    if not validation["success"]:

        repair_log.append({
            "stage": "appspec",
            "status": "repair_attempted"
        })

        appspec = repair_appspec(
            appspec,
            validation["errors"]
        )

        validation = validate_appspec(appspec)
    cost_breakdown = {
        "intent_extraction": COST_TABLE["gpt-4o-mini"],
        "schema_generation": COST_TABLE["gpt-4o"],
        "appspec_generation": COST_TABLE["gpt-4o"]
    }
    latency = {
        "intent_extraction":
            round(intent_time - start_time, 3),

        "schema_generation":
            round(schema_time - intent_time, 3),

        "appspec_generation":
            round(appspec_time - schema_time, 3)
    }
    return {

        "intent": intent,

        "schema": schema,

        "appspec": appspec,

        "validation": validation,

        "repair_log": repair_log,
        "cost_breakdown": cost_breakdown,
        "latency": latency,
        "trace_log": trace_log
    }