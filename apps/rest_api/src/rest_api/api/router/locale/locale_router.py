from fastapi import APIRouter

router = APIRouter(prefix="/v1/locale", tags=["locale", "region"])


@router.get(
    "/{locale_tag}",
    response_model=dict,
    description="Get the default locale information",
    response_model_exclude_none=True,
)
async def get_locale(locale_tag: str) -> dict:
    # language = LanguageDto(
    #     code=locale_tag.split("-")[0],
    #     name="English",
    #     name_local="English",
    #     script="Latn",
    #     text_direction=TextDirection.LTR,
    #     fallback_chain=["en"],
    # )
    return {"tag": "en-US", "language": "en", "region": "US", "script": "Latn"}
