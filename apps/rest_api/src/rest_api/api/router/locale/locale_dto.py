from pydantic import BaseModel, Field

from rest_api.api.router.language.language_dto import Language


class Locale(BaseModel):
    """
    A locale represents a specific linguistic and regional setting,
    typically used for internationalization and localization purposes.
    """

    locale: str = Field(
        ...,
        description="RFC 5646 language tag with optional script and region subtag",
        examples=["en-US", "zh-Hant-TW", "fr-FR"],
    )

    language: Language = Field(
        ..., description="The language associated with this locale"
    )
