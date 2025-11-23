from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Configuration(BaseSettings):
    """Application configuration loaded in order (overwriting) from: defaults, .env file, environment variables."""

    # ---- meta ---
    environment: str = Field(default="dev")
    debug: bool = Field(default=False)

    # ---- API ----
    host: str = Field(default="0.0.0.0")
    port: int = Field(default=8080)

    # ---- DB ----
    ## FIXME: use `Optional[PostgresDsn] = None` in future
    async_database_url: Optional[str] = None

    # ---- Logging ----
    log_level: str = Field(default="INFO")

    # ---- Time ----
    default_timezone: str = Field(default="UTC")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        validate_default=True,
        extra="ignore",
    )


configuration = Configuration()
