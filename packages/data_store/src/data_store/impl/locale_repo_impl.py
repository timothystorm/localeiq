from typing import Sequence, Optional

from sqlalchemy import select

from data_store.dto.locale_dto import LocaleDto, LocaleFilter
from data_store.repository.locale_repo import LocaleRepo
from data_store.schema.locale_bronze_schema import LocaleBronzeLocale as LocaleSchema
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
        self, filters: Optional[LocaleFilter] = None
    ) -> Sequence[LocaleDto]:
        filters = filters or LocaleFilter()

        with read_only_session() as session:
            # Build SELECT (core) query
            stmt = select(
                LocaleSchema.tag,
                LocaleSchema.language,
                LocaleSchema.script,
                LocaleSchema.region,
            ).order_by(LocaleSchema.tag)

            # Apply filters
            for field, column in _FILTER_DICT.items():
                value = getattr(filters, field)
                if value:
                    stmt = stmt.where(column.__eq__(value))

            # Execute query
            rows = session.execute(stmt).mappings().all()
            return [LocaleDto(**row) for row in rows]
