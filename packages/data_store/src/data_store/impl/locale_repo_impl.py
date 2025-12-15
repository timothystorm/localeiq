from typing import Sequence

from sqlalchemy import select

from data_store.dto.locale_dto import LocaleDto
from data_store.repository.locale_repo import LocaleRepo
from data_store.schema.locale_bronze_schema import LocaleBronzeLocale as LocaleSchema
from data_store.transaction import read_only_session


class LocaleRepoImpl(LocaleRepo):
    def read_all(self) -> Sequence[LocaleDto]:
        with read_only_session() as session:
            stmt = select(
                LocaleSchema.tag,
                LocaleSchema.language,
                LocaleSchema.script,
                LocaleSchema.region,
            ).order_by(LocaleSchema.tag)
            rows = session.execute(stmt).mappings()
            return [LocaleDto(**row) for row in rows]

    def read_by_language(self, language: str) -> Sequence[LocaleDto]:
        print(language)
        with read_only_session() as session:
            stmt = (
                select(
                    LocaleSchema.tag,
                    LocaleSchema.language,
                    LocaleSchema.script,
                    LocaleSchema.region,
                )
                .order_by(LocaleSchema.tag)
                .where(LocaleSchema.language.__eq__(language))
            )
            rows = session.execute(stmt).mappings()
            return [LocaleDto(**row) for row in rows]
