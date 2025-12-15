from typing import Optional, Sequence, Annotated

from fastapi import APIRouter, Depends
from fastapi.params import Query

from data_store.dto.locale_dto import LocaleDto
from data_store.repository.provider import get_locale_repository
from rest_api.service.locale.locale_service import LocaleService

router = APIRouter(prefix="/v1/locale", tags=["locale"])


def get_locale_service() -> LocaleService:
    """DI for LocaleService"""
    return LocaleService(get_locale_repository())


@router.get(
    "/",
    response_model=Sequence[LocaleDto],
    description="Get locales supported by LocaleIQ",
    response_model_exclude_none=True,
)
async def get_locales(
    language: Annotated[
        Optional[str],
        Query(
            None,
            description="Filter locales by language tag",
            examples=["en", "zh", "de"],
        ),
    ] = None,
    service: LocaleService = Depends(get_locale_service),
) -> Sequence[LocaleDto]:
    return service.get_locales(language)
