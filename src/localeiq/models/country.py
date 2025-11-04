from pydantic import BaseModel

"""
Model representing a country with its code and name.
"""
class Country(BaseModel):
    code: str
    name: str
