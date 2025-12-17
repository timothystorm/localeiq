# locale/domain/locale_query.py
from typing import Optional
from typing import Sequence

from pydantic import BaseModel, field_validator

from data_store.dto.cursor_dto import CursorDto, Cursor
from data_store.dto.locale_dto import LocaleDto, LocaleFilter
from data_store.repository.locale_repo import LocaleRepo
from data_store.utils.normalize_locale_tag import normalize_locale_tag


class LocaleQuery(BaseModel):
    language: Optional[str] = None
    region: Optional[str] = None
    script: Optional[str] = None
    after: Optional[str] = None
    limit: Optional[int] = 1000

    @field_validator("after", mode="before")
    @classmethod
    def normalize_after(cls, v):
        return normalize_locale_tag(v) if v else v

    @field_validator("limit")
    @classmethod
    def validate_limit(cls, v):
        if v <= 0:
            raise ValueError("limit must be positive")
        if v > 1000:
            raise ValueError("limit exceeds maximum allowed value")
        return v


class LocaleService:
    """
    Service for handling locale-related operations and business logic.
    """

    def __init__(self, repo: LocaleRepo):
        self._repo = repo

    def get_locales(
        self,
        *,
        query: LocaleQuery,
    ) -> CursorDto[Sequence[LocaleDto]]:
        """
        :param query: optional filters and cursor to apply when retrieving locales.
        :return:
        """
        return self._repo.read_locale(
            filters=LocaleFilter(
                language=query.language, region=query.region, script=query.script
            ),
            cursor=Cursor(limit=query.limit, after=query.after),
        )
