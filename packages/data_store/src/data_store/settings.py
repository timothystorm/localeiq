from functools import lru_cache
from pathlib import Path
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


def _get_default_env_path() -> str:
    """Get default .env path, two levels up from this file."""
    return str(Path(__file__).resolve().parents[2] / ".env")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=_get_default_env_path(), env_file_encoding="utf-8", extra="ignore"
    )

    DB_HOST: Optional[str] = None
    DB_NAME: Optional[str] = None
    DB_PASSWORD: Optional[str] = None
    DB_PORT: Optional[int] = None
    DB_USER: Optional[str] = None
    DB_URL: Optional[str] = None

    @property
    def db_url(self) -> str:
        if self.DB_URL:
            return self.DB_URL
        raise RuntimeError("DB_URL not provided in environment")


@lru_cache
def get_settings() -> Settings:
    """
    Cached settings factory. Use this for dependency injection.
    The lru_cache ensures singleton behavior but allows overriding in tests.
    """
    return Settings()
