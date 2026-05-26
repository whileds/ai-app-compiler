from models import AppSchema


def validate_schema(data):

    try:
        validated = AppSchema(**data)
        return {
            "success": True,
            "data": validated.dict()
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }