from pydantic import BaseModel, Field

from data_store.dto.language_dto import LanguageDto


class Locale(BaseModel):
    """
    A locale represents a specific linguistic and regional setting,
    typically used for internationalization and localization.
    """

    locale: str = Field(
        ...,
        description="RFC 5646 language tag with optional script and region subtag",
        examples=["en-US", "zh-Hant-TW", "fr-FR"],
    )

    language: LanguageDto
