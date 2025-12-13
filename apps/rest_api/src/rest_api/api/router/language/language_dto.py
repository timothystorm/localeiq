from enum import Enum

from pydantic import BaseModel, Field


class TextDirection(Enum):
    LTR = "ltr"
    RTL = "rtl"


class Language(BaseModel):
    code: str = Field(
        ..., description="ISO 639 language code", examples=["en", "zh", "fr"]
    )
    name: str = Field(
        ...,
        description="English name of the language",
        examples=["English", "Chinese", "French"],
    )
    name_local: str = Field(
        ...,
        description="Localized name of the language",
        examples=["English", "中文", "Français"],
    )
    script: str = Field(
        ...,
        description="Script used by the language",
        examples=["Latn", "Hant", "Cyrl"],
    )
    text_direction: TextDirection
    fallback_chain: list[str] = Field(
        ...,
        description="Ordered list of fallback language codes",
        examples=[["zh-CN", "zh-Hans", "zh", "root"], ["en-US", "en", "root"]],
    )
