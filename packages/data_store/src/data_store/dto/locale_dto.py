from pydantic import BaseModel


class LocaleDto(BaseModel):
    tag: str
    language: str
    script: str | None
    region: str | None
