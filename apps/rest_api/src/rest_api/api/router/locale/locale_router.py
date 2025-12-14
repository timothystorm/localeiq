from typing import Optional

from fastapi import APIRouter

from data_store.dto.locale_dto import LocaleDto
from rest_api.service.locale.locale_service import LocaleService

router = APIRouter(prefix="/v1/locale", tags=["language", "locale", "region"])


@router.get(
    "/",
    response_model=list[LocaleDto],
    description="Get all the locales supported by LocaleIQ",
    response_model_exclude_none=True,
)
async def get_locales(language: Optional[str] = None) -> list[LocaleDto]:
    return LocaleService.get_locales(language)
