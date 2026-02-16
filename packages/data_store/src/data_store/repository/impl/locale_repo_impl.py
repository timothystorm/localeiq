from typing import Sequence, Optional

from sqlalchemy import select

from data_store.dto.cursor_dto import Cursor, CursorDto
from data_store.dto.locale_dto import LocaleDto, LocaleFilter
from data_store.repository.locale_repo import LocaleRepo
from data_store.schema.bronze.locale_bronze_schema import (
    LocaleBronzeSchema as LocaleSchema,
)
from data_store.transaction import read_only_session

"""
Mapping of filter fields to their corresponding schema
"""
_FILTER_DICT = {
    "language": LocaleSchema.language,
    "region": LocaleSchema.region,
    "script": LocaleSchema.script,
}


class LocaleRepoImpl(LocaleRepo):
    def read_locale(
        self, *, filters: LocaleFilter, cursor: Optional[Cursor] = None
    ) -> CursorDto[Sequence[LocaleDto]]:
        filters = filters or LocaleFilter()
        with read_only_session() as session:
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

            # Apply pagination
            if cursor:
                aft = cursor.after
                lmt = cursor.limit
                if aft:
                    stmt = stmt.where(LocaleSchema.locale > aft)
                if lmt:
                    # fetch one extra to detect "more"
                    stmt = stmt.limit(lmt + 1)

            # Execute query
            rows = session.execute(stmt).mappings().all()

            # Construct response
            has_more = len(rows) > lmt if lmt else False
            items = rows[:lmt] if lmt else rows
            next_val = str(items[-1]["locale"]) if has_more and items else None
            return CursorDto(next=next_val, data=[LocaleDto(**row) for row in items])
