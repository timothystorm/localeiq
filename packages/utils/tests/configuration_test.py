from pathlib import Path

import pytest
from pydantic import ValidationError

from utils.configuration import get_config, EnvironmentEnum


class TestDefaultConfig:
    @pytest.fixture(autouse=True)
    def setup_environment(self):
        yield  # run tests

        get_config.cache_clear()

    def test_create(self):
        """Ensures that the default configuration loads successfully."""
        try:
            get_config()
        except ValidationError:
            assert False, "Loading default configuration should not raise an error"


class TestEnvVariableConfig:
    @pytest.fixture(autouse=True)
    def setup_environment(self, monkeypatch):
        """
        Ensure environment variables override default values
        when Configuration is instantiated.
        """

        # ---- Set env vars before config instantiation ----
        monkeypatch.setenv("ENVIRONMENT", "production")
        monkeypatch.setenv("DEFAULT_TIMEZONE", "Saturn/Io")
        monkeypatch.setenv("PORT", "3000")

        yield  # run tests

        # clear cache after each run
        get_config.cache_clear()

    def test_load_from_env(self):
        cfg = get_config()  # loads from env + .env + defaults

        # ---- Assertions ----
        assert cfg.environment == "production"
        assert cfg.environment == EnvironmentEnum.production
        assert cfg.is_production() is True
        assert cfg.default_timezone == "Saturn/Io"
        assert cfg.port == 3000  # env overrides default 8080
        assert cfg.host == "0.0.0.0"  # still default


class TestWithEnvFile:
    @pytest.fixture(autouse=True)
    def setup_environment(self, monkeypatch, tmp_path: Path):
        # ---- create a temporary .env file ----
        env_file = tmp_path / ".env"
        env_file.write_text(
            "DEFAULT_TIMEZONE=Mars/Olympus_Mons\n"
            "PORT=9001\n"
            "non_existent=setting\n"
        )

        # ---- point Pydantic's env_file path to our temp file ----
        monkeypatch.setenv("ENV_FILE", str(env_file))

        # Pydantic doesn't use ENV_FILE by default, so we temporarily
        # change working directory to tmp_path so `.env` is discovered.
        monkeypatch.chdir(tmp_path)

        yield  # run tests

        # clear cache after each run
        get_config.cache_clear()

    def test_load_env_file(self):
        """Ensures that the .env configuration(s) works"""
        cfg = get_config()

        # ---- Assertions ----
        assert cfg.default_timezone == "Mars/Olympus_Mons"
        assert cfg.port == 9001  # env overrides default 8080
        assert cfg.environment == "dev"  # unchanged default
        assert cfg.environment == EnvironmentEnum.dev

        with pytest.raises(AttributeError):
            # not defined in Configuration
            _ = cfg.non_existent

    def test_env_file_and_env_vars(self, monkeypatch):
        # ---- Override with environment variable ----
        monkeypatch.setenv("port", "5432")

        cfg = get_config()

        # ---- Assertions ----
        assert cfg.host == "0.0.0.0"  # default
        assert cfg.port == 5432 # env var wins
        assert cfg.default_timezone == "Mars/Olympus_Mons"  # from .env
