
# from fastapi import FastAPI
# from pydantic import BaseModel

# from generator import generate_app_schema
# from validator import validate_schema

# app = FastAPI()


# class UserPrompt(BaseModel):
#     prompt: str


# @app.get("/")
# def home():
#     return {"message": "AI App Compiler Running"}


# @app.post("/generate")
# def generate(user_input: UserPrompt):

#     generated_schema = generate_app_schema(user_input.prompt)

#     validated = validate_schema(generated_schema)

#     return validated







from fastapi import FastAPI
from pydantic import BaseModel
from frontend_generator import generate_frontend
from generator import generate_app_schema
from validator import validate_schema
from repair_engine import repair_schema

app = FastAPI()


class UserPrompt(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {
        "message": "AI App Compiler Running"
    }


@app.post("/generate")
def generate(user_input: UserPrompt):

    generated_schema = generate_app_schema(user_input.prompt)

    validation_result = validate_schema(generated_schema)

    if not validation_result["success"]:

        repaired = repair_schema(generated_schema)

        validation_result = validate_schema(repaired)

        return {
            "status": "repaired",
            "result": validation_result
        }
    frontend = generate_frontend(generated_schema)
    return {
        "status": "valid",
        "result": validation_result,
        "frontend_code": frontend
    }
