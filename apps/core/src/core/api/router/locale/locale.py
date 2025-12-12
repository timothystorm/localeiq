from pydantic import BaseModel, Field

from core.api.router.language.language import Language


class Locale(BaseModel):
    """
    A locale represents a specific linguistic and regional setting,
    typically used for internationalization and localization purposes.
    """

    locale: str = Field(
        ...,
        description="ISO 639 language code with optional script and region subtags",
        examples=["en-US", "zh-Hant-TW", "fr-FR"],
    )

    language: Language = Field(
        ..., description="The language associated with this locale"
    )
