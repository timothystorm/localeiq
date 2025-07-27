from pydantic import BaseModel

from localeiq.models.country import Country


class Location(BaseModel):
    country: Country
    city: str
    postal_code: str
