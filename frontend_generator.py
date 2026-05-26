def generate_frontend(schema):

    pages = schema.get("pages", [])

    frontend_code = {}

    for page in pages:

        component = f"""
function {page}() {{
    return (
        <div>
            <h1>{page} Page</h1>
        </div>
    );
}}

export default {page};
"""

        frontend_code[f"{page}.jsx"] = component

    return frontend_code