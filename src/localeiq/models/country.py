from pydantic import BaseModel

class CountryName(BaseModel):
    name: str