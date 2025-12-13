from typing import Any

from sqlalchemy import select

from data_store.connection import engine
from data_store.models import CountryBronze


def read_countries() -> Any:
    with engine.connect().execution_options(isolation_level="AUTOCOMMIT") as conn:
        result = conn.execute(select(CountryBronze))
        return [dict(row) for row in result.mappings()]
