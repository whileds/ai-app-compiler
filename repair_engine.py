def repair_appspec(appspec, validation_errors):

    for error in validation_errors:

        if error["type"] == "PAGE_API_MISMATCH":

            entity = error["message"].split("for ")[1]

            appspec["apiEndpoints"].append({
                "path": f"/api/{entity.lower()}",
                "method": "GET",
                "entity": entity,
                "authRequired": True
            })

    return appspec