from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data_store.settings import settings

# Create the SQLAlchemy engine using the database URL from settings
engine = create_engine(
    settings.db_url,
    echo=False,
    future=True,
    pool_pre_ping=True,
)

# Create a configured "Session" class
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)
