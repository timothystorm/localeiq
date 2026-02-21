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
Mapping of filter fields to their corresponding schema
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
            value = getattr(filters, field)
            if value:
                stmt = stmt.where(column.__eq__(value))

        # Apply pagination with enforced limits
        lmt = MAX_PAGINATION_LIMIT  # Default limit
        if cursor and cursor.limit is not None:
            lmt = min(cursor.limit, MAX_PAGINATION_LIMIT)

        if cursor and cursor.after:
            stmt = stmt.where(LocaleSchema.locale > cursor.after)

        # Always apply limit (fetch one extra to detect "more")
        stmt = stmt.limit(lmt + 1)

        # Execute query
        rows = self._session.execute(stmt).mappings().all()

        # Construct response
        has_more = len(rows) > lmt
        items = rows[:lmt]
        next_val = str(items[-1]["locale"]) if has_more and items else None
        return CursorDto(next=next_val, data=[LocaleDto(**row) for row in items])
