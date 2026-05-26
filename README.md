# AI App Compiler

A multi-stage AI system that converts natural language into structured application schemas.

## Features

- Intent Extraction
- Schema Generation
- Validation Engine
- Repair Engine
- Deterministic JSON Output
- Executable FastAPI Runtime

## Tech Stack

- FastAPI
- Python
- Pydantic

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## API Endpoint

POST `/generate`

Example:

```json
{
  "prompt": "Build CRM with login and dashboard"
}
```
