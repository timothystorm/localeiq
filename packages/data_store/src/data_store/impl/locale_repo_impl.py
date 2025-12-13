from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from data_store.dto.locale_dto import LocaleDto
from data_store.repository.locale_repo import LocaleRepo
from data_store.schema.locale_bronze_schema import LocaleBronzeLocale as LocaleSchema


class LocaleRepoImpl(LocaleRepo):
    def __init__(self, session: Session):
        self._session = session

    def read_all(self) -> Sequence[LocaleDto]:
        stmt = select(
            LocaleSchema.tag,
            LocaleSchema.language,
            LocaleSchema.script,
            LocaleSchema.region,
        )
        rows = self._session.execute(stmt).mappings()
        return [LocaleDto(**row) for row in rows]
