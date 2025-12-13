from fastapi import APIRouter

from rest_api.api.router.language.language_dto import Language, TextDirection
from rest_api.api.router.locale.locale_dto import Locale

router = APIRouter(prefix="/v1/locale", tags=["locale", "region"])


@router.get(
    "/{locale_tag}",
    response_model=Locale,
    description="Get the default locale information",
    response_model_exclude_none=True,
)
async def get_locale(locale_tag: str) -> Locale:
    language = Language(
        code=locale_tag.split("-")[0],
        name="English",
        name_local="English",
        script="Latn",
        text_direction=TextDirection.LTR,
        fallback_chain=["en"],
    )
    return Locale(locale=locale_tag, language=language)
