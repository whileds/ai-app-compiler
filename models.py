from pydantic import BaseModel
from typing import List


class APIEndpoint(BaseModel):
    path: str
    method: str


class DatabaseTable(BaseModel):
    name: str
    columns: List[str]


class AppSchema(BaseModel):
    app_name: str
    pages: List[str]
    apis: List[APIEndpoint]
    database: List[DatabaseTable]