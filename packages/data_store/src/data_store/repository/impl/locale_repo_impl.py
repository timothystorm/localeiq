from typing import Sequence, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from data_store.dto.cursor_dto import Cursor, CursorDto
from data_store.dto.locale_dto import LocaleDto, LocaleFilter
from data_store.repository.locale_repo import LocaleRepo
from data_store.schema.bronze.locale_bronze_schema import (
    LocaleBronzeSchema as LocaleSchema,
)

"""
Mapping of filter fields to corresponding schema
"""
_FILTER_DICT = {
    "language": LocaleSchema.language,
    "region": LocaleSchema.region,
    "script": LocaleSchema.script,
}

# Maximum allowed limit to prevent OOM
MAX_PAGINATION_LIMIT = 1000


class LocaleRepoImpl(LocaleRepo):
    def __init__(self, session: Session):
        self._session = session

    def read_locale(
        self, *, filters: LocaleFilter, cursor: Optional[Cursor] = None
    ) -> CursorDto[Sequence[LocaleDto]]:
        filters = filters or LocaleFilter()
        page_limit = min(
            (cursor.limit if cursor and cursor.limit else MAX_PAGINATION_LIMIT),
            MAX_PAGINATION_LIMIT,
        )

        # Build SELECT query
        stmt = select(
            LocaleSchema.id,
            LocaleSchema.locale,
            LocaleSchema.language,
            LocaleSchema.script,
            LocaleSchema.region,
        ).order_by(LocaleSchema.locale, LocaleSchema.id)

        # Apply filters
        for field, column in _FILTER_DICT.items():
            if value := getattr(filters, field, None):
                stmt = stmt.where(column.__eq__(value))

        # Apply cursor-based filtering for pagination
        if cursor and cursor.after:
            stmt = stmt.where(LocaleSchema.locale > cursor.after)

        # Fetch one extra record to determine if there's a next page
        stmt = stmt.limit(page_limit + 1)

        # Execute query
        results = self._session.execute(stmt).mappings().all()
        items = [LocaleDto.model_validate(row) for row in results]

        # Determine next cursor
        has_more = len(items) > page_limit
        next_cursor = items[page_limit - 1].locale if has_more else None

        # Return paginated and mapped response
        return CursorDto(next=next_cursor, data=items[:page_limit])
