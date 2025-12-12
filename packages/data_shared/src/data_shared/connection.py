from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data_shared.settings import settings

engine = create_engine(settings.db_url, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
