from pydantic import BaseModel, Field


class Subdivision(BaseModel):
    code: str = Field(
        ...,
        description="ISO 3166-2 subdivision code",
        examples=["CA", "BJ", "IDF", "MH"],
    )
    name: str = Field(
        ...,
        description="English name of the subdivision",
        examples=["California", "Beijing", "Island of France", "Maharashtra"],
    )
    name_local: str = Field(
        ...,
        description="Localized name of the subdivision",
        examples=["California", "北京", "Île-de-France", "महाराष्ट्र"],
    )
    type: str = Field(
        ...,
        description="Type of subdivision",
        examples=["State", "Province", "Region", "State", "Federal District"],
    )
