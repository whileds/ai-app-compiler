def repair_schema(data):

    if "app_name" not in data:
        data["app_name"] = "Recovered App"

    if "pages" not in data:
        data["pages"] = []

    if "apis" not in data:
        data["apis"] = []

    if "database" not in data:
        data["database"] = []

    return data