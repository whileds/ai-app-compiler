# def generate_schema(app_intent):

#     entities = []

#     app_type = app_intent.get("appType")

#     if app_type == "crm":

#         entities = [

#             {
#                 "name": "Lead",
#                 "tableName": "leads",
#                 "fields": [
#                     "id",
#                     "name",
#                     "email",
#                     "phone",
#                     "tenantId"
#                 ]
#             },

#             {
#                 "name": "Deal",
#                 "tableName": "deals",
#                 "fields": [
#                     "id",
#                     "amount",
#                     "status",
#                     "tenantId"
#                 ]
#             }
#         ]

#     elif app_type == "ecommerce":

#         entities = [

#             {
#                 "name": "Product",
#                 "tableName": "products",
#                 "fields": [
#                     "id",
#                     "name",
#                     "price",
#                     "stock",
#                     "tenantId"
#                 ]
#             },

#             {
#                 "name": "Order",
#                 "tableName": "orders",
#                 "fields": [
#                     "id",
#                     "total",
#                     "status",
#                     "tenantId"
#                 ]
#             }
#         ]

#     elif app_type == "inventory":

#         entities = [

#             {
#                 "name": "Product",
#                 "tableName": "inventory_products",
#                 "fields": [
#                     "id",
#                     "name",
#                     "quantity",
#                     "supplier",
#                     "tenantId"
#                 ]
#             },

#             {
#                 "name": "StockMovement",
#                 "tableName": "stock_movements",
#                 "fields": [
#                     "id",
#                     "type",
#                     "quantity",
#                     "tenantId"
#                 ]
#             }
#         ]

#     elif app_type == "project_management":

#         entities = [

#             {
#                 "name": "Project",
#                 "tableName": "projects",
#                 "fields": [
#                     "id",
#                     "name",
#                     "deadline",
#                     "tenantId"
#                 ]
#             },

#             {
#                 "name": "Task",
#                 "tableName": "tasks",
#                 "fields": [
#                     "id",
#                     "title",
#                     "status",
#                     "priority",
#                     "tenantId"
#                 ]
#             }
#         ]

#     elif app_type == "hr_tool":

#         entities = [

#             {
#                 "name": "Employee",
#                 "tableName": "employees",
#                 "fields": [
#                     "id",
#                     "name",
#                     "department",
#                     "tenantId"
#                 ]
#             },

#             {
#                 "name": "LeaveRequest",
#                 "tableName": "leave_requests",
#                 "fields": [
#                     "id",
#                     "status",
#                     "reason",
#                     "tenantId"
#                 ]
#             }
#         ]

#     elif app_type == "analytics":

#         entities = [

#             {
#                 "name": "Report",
#                 "tableName": "reports",
#                 "fields": [
#                     "id",
#                     "title",
#                     "metric",
#                     "tenantId"
#                 ]
#             }
#         ]

#     else:

#         entities = [

#             {
#                 "name": "CustomEntity",
#                 "tableName": "custom_entities",
#                 "fields": [
#                     "id",
#                     "name",
#                     "tenantId"
#                 ]
#             }
#         ]

#     return {
#         "entities": entities
#     }


# def generate_schema(app_intent):

#     entities = []

#     extracted_entities = app_intent.get("entities", [])

#     if extracted_entities:

#         for entity in extracted_entities:

#             entities.append(
#                 {
#                     "name": entity,
#                     "tableName": entity.lower().replace(" ", "_") + "s",
#                     "fields": [
#                         "id",
#                         "name",
#                         "tenantId"
#                     ]
#                 }
#             )

#     else:

#         entities = [
#             {
#                 "name": "CustomEntity",
#                 "tableName": "custom_entities",
#                 "fields": [
#                     "id",
#                     "name",
#                     "tenantId"
#                 ]
#             }
#         ]

#     return {
#         "entities": entities
#     }









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