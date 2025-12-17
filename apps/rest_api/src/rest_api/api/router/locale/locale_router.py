from typing import Sequence

from fastapi import APIRouter, Depends

from data_store.dto.cursor_dto import CursorDto
from data_store.dto.locale_dto import LocaleDto
from data_store.repository.provider import get_locale_repository
from rest_api.dto.api_dto import Meta, StandardResponse, Page
from rest_api.service.locale.locale_service import LocaleService, LocaleQuery

router = APIRouter(prefix="/v1/locale", tags=["locale"])


def get_locale_service() -> LocaleService:
    """DI for LocaleService"""
    return LocaleService(get_locale_repository())


@router.get(
    "/",
    description="Get locales supported by LocaleIQ",
    response_model_exclude_none=True,
)
async def get_locales(
    query: LocaleQuery = Depends(),
    service: LocaleService = Depends(get_locale_service),
) -> StandardResponse[Sequence[LocaleDto]]:
    response: CursorDto[Sequence[LocaleDto]] = service.get_locales(query=query)

    # Construct meta-information
    meta: Meta = {"page": Page(size=len(response.data), cursor=response.next or None)}
    # TODO: Make query param responses part of a debugging option
    # if query:
    #     dumped = query.model_dump(exclude_none=True)
    #     if any(v != "" for v in dumped.values()):
    #         meta["query"] = dumped

    # Construct response
    return StandardResponse(
        meta=meta,
        data=response.data,
    )
