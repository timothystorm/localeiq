from pydantic import BaseModel


class RootContext(BaseModel):
    name: str
    version: str
    description: str
