import json


def generate_app_schema(user_prompt: str):

    prompt = user_prompt.lower()

    pages = ["Home"]

    apis = []

    database = []

    if "login" in prompt:
        pages.append("Login")

        apis.append({
            "path": "/login",
            "method": "POST"
        })

        database.append({
            "name": "users",
            "columns": ["id", "email", "password"]
        })

    if "dashboard" in prompt:
        pages.append("Dashboard")

    if "payment" in prompt:
        apis.append({
            "path": "/payment",
            "method": "POST"
        })

        database.append({
            "name": "payments",
            "columns": ["id", "amount", "user_id"]
        })
    if "hospital" in prompt:
        pages.append("Doctor Panel")
        pages.append("Patient Records")
        apis.append({
            "path": "/doctors",
            "method": "GET"
       })
        database.append({
            "name": "patients",
            "columns": ["id", "name", "disease"]
        })
    if "ecommerce" in prompt:
        pages.append("Products")
        pages.append("Cart")

        apis.append({
            "path": "/products",
            "method": "GET"
    })
        database.append({
            "name": "products",
            "columns": ["id", "name", "price"]
        })

    return {
        "app_name": "Generated App",
        "pages": pages,
        "apis": apis,
        "database": database
    }