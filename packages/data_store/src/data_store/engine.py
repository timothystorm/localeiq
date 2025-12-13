from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data_store.settings import settings

engine = create_engine(
    settings.db_url,
    echo=False,
    future=True,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)
