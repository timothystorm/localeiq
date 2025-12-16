from typing import Any, TypedDict, NotRequired

from fastapi import APIRouter, Depends

from data_store.dto.locale_dto import LocaleFilter
from data_store.repository.provider import get_locale_repository
from rest_api.service.locale.locale_service import LocaleService

router = APIRouter(prefix="/v1/locale", tags=["locale"])


# TODO: Move to a common dto package
class MetaDict(TypedDict):
    count: int
    filters: NotRequired[dict[str, Any]]


def get_locale_service() -> LocaleService:
    """DI for LocaleService"""
    return LocaleService(get_locale_repository())


@router.get(
    "/",
    response_model=dict[str, Any],
    description="Get locales supported by LocaleIQ",
    response_model_exclude_none=True,
)
async def get_locales(
    filters: LocaleFilter = Depends(),
    service: LocaleService = Depends(get_locale_service),
) -> dict[str, Any]:
    print(filters)
    locales = service.get_locales(filters)

    # Construct meta-information
    meta: MetaDict = {"count": len(locales)}
    if filters is not None:
        dumped = filters.model_dump(exclude_none=True)
        if any(v != "" for v in dumped.values()):
            meta["filters"] = dumped

    # Return meta + response
    return {"meta": meta, "data": [locale.model_dump() for locale in locales]}
