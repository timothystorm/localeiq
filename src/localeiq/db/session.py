from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from localeiq.util.configs import DATABASE_URL

engine = create_async_engine(url=DATABASE_URL, pool_pre_ping=True)
SessionLocal = async_sessionmaker(
    bind=engine, expire_on_commit=False, class_=AsyncSession
)


@asynccontextmanager
async def db_session() -> AsyncGenerator[AsyncSession | Any, Any]:
    async with SessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
