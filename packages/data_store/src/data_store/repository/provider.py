from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from data_store.engine import get_db_session
from data_store.repository.impl.locale_repo_impl import LocaleRepoImpl
from data_store.repository.locale_repo import LocaleRepo


def get_locale_repository(
    session: Annotated[Session, Depends(get_db_session)],
) -> LocaleRepo:
    """
    FastAPI dependency for LocaleRepo with proper session lifecycle.
    Session is managed by FastAPI and properly closed after request.
    """
    return LocaleRepoImpl(session)
