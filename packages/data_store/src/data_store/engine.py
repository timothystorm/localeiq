from typing import Generator, Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from data_store.settings import Settings, get_settings

_engine = None
_SessionLocal = None


def get_engine(settings: Settings):
    """Get or create SQLAlchemy engine based on settings."""
    global _engine
    if _engine is None:
        _engine = create_engine(
            settings.db_url,
            echo=False,
            future=True,
            pool_pre_ping=True,
        )
    return _engine


def get_session_factory(settings: Settings) -> sessionmaker:
    """Get or create session factory."""
    global _SessionLocal
    if _SessionLocal is None:
        engine = get_engine(settings)
        _SessionLocal = sessionmaker(
            bind=engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )
    return _SessionLocal


def get_db_session(
    settings: Optional[Settings] = None,
) -> Generator[Session, None, None]:
    """
    Dependency for getting a database session.
    Use this in FastAPI Depends() for proper lifecycle management.
    """
    if settings is None:
        settings = get_settings()
    SessionFactory = get_session_factory(settings)
    session = SessionFactory()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
