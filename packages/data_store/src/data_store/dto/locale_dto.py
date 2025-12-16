from typing import Optional

from pydantic import BaseModel, field_validator


class LocaleFilter(BaseModel):
    """
    Filter the model for locale data with built-in normalization.
    """

    language: Optional[str] = None
    region: Optional[str] = None
    script: Optional[str] = None

    @field_validator("language", mode="before")
    @classmethod
    def normalize_language(cls, v):
        return v.lower() if v else v

    @field_validator("region", mode="before")
    @classmethod
    def normalize_region(cls, v):
        return v.upper() if v else v

    @field_validator("script", mode="before")
    @classmethod
    def normalize_script(cls, v):
        return v.capitalize() if v else v


class LocaleDto(BaseModel):
    tag: str
    language: str
    script: str | None
    region: str | None
