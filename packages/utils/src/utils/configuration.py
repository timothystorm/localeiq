from enum import Enum
from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvironmentEnum(str, Enum):
    """
    Application environment enum.
    """
    dev = "dev"
    staging = "staging"
    production = "production"


class Configuration(BaseSettings):
    """
        Application configuration loaded in order (overwriting) from: defaults, .env file, environment variables.

        Use `get_localeiq_config()` for app-wide configuration. Direct instantiation is supported for testing and tooling.
        """

    # ---- meta ---
    environment: EnvironmentEnum = Field(default=EnvironmentEnum.dev)
    debug: bool = Field(default=False)

    # ---- API ----
    host: str = "0.0.0.0"
    port: int = 8080

    # ---- DB ----
    # async_database_url: Optional[str] = None

    # # ---- Logging ----
    # log_level: str = "INFO"

    # ---- Time ----
    default_timezone: str = Field(default="UTC", description="Default IANA timezone to use")

    # ---- Loads .env ---
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        validate_default=True,
        extra="ignore",
    )

    def is_production(self) -> bool:
        return self.environment != EnvironmentEnum.dev and self.environment != EnvironmentEnum.staging


@lru_cache
def get_config() -> Configuration:
    """
    Global accessor for application configuration.
    Loaded once, cached forever unless manually cleared.

    Production:
        config = get_localeiq_config() # load or pull from cache
        get_localeiq_config.cache_clear() # clear cache and reload configs
    """
    return Configuration()
