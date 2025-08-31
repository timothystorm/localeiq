import os
from pathlib import Path

from dotenv import load_dotenv

# Always resolve relative to project root (e.g. where pyproject.toml is)
BASE_DIR = Path(__file__).resolve().parents[3]
env_path = BASE_DIR / ".env"

load_dotenv(dotenv_path=env_path, override=True)

DATABASE_URL = os.getenv("ASYNC_DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError(f"Missing 'ASYNC_DATABASE_URL' in {env_path}")
