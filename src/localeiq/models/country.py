from pydantic import BaseModel


class Country(BaseModel):
    code: str
    name: str


class CountryCountResponse(BaseModel):
    count: int
