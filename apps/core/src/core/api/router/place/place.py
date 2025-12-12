from pydantic import BaseModel, Field


class Subdivision(BaseModel):
    code: str = Field(
        ...,
        description="ISO 639 language code",
        examples=["US-CA", "CN-BJ", "FR-IDF", "IN-MH"],
    )
    name: str = Field(
        ...,
        description="English name of the subdivision",
        examples=["California", "Beijing", "Île-de-France", "Maharashtra"],
    )
    name_local: str = Field(
        ...,
        description="Localized name of the subdivision",
        examples=["California", "北京", "Île-de-France", "महाराष्ट्र"],
    )
    type: str = Field(
        ...,
        description="Type of subdivision",
        examples=["State", "Province", "Region", "State"],
    )
