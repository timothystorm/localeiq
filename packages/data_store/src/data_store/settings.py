from pathlib import Path
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

# The .env file is expected to be located two levels up from this file, i.e., at the root of the project.
BASE_ENV = Path(__file__).resolve().parents[2] / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(BASE_ENV), env_file_encoding="utf-8", extra="ignore"
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


settings = Settings()
