# LocaleIQ Development Guide

LocaleIQ is a FastAPI-based REST API providing chronology, time, timezone, and locale management services. The project uses a **Poetry monorepo** architecture with strict submodule isolation.

## Architecture Overview

### Monorepo Structure

```
localeiq/
├── apps/              # Standalone applications
│   ├── rest_api/      # FastAPI REST API (FastAPI, Uvicorn, Pydantic)
│   └── cli_tool/      # Command-line interface
├── packages/          # Shared libraries
│   ├── data_store/    # Database layer (PostgreSQL, Alembic)
│   └── utils/         # Common utilities
└── pyproject.toml     # Root (editor integration only, NO runtime deps)
```

### Critical: Root vs Submodule pyproject.toml

- **Root `pyproject.toml`**: Editor integration and dev tools ONLY. Do NOT add runtime dependencies here.
- **Submodule `pyproject.toml`**: Each app/package has its own with real dependencies.
- All submodules use `poetry.lock` from the root (no individual lock files).

### Layer Architecture

```
rest_api/
├── api/           # FastAPI layer (routers, middleware)
│   ├── router/    # Route handlers (time, timezone, locale)
│   └── middleware/ # Request middleware (TracerMiddleware, TimerMiddleware)
├── service/       # Business logic (chrono, locale services)
└── dto/           # Data transfer objects

data_store/
├── repository/    # Abstract repository interfaces
├── impl/          # Concrete implementations (LocaleRepoImpl)
├── schema/        # SQLAlchemy models
└── engine.py      # Database connection management
```

Repository pattern: `provider.py` returns repository instances (e.g., `get_locale_repository()`).

## Build, Test, and Lint Commands

### Root Level (All Submodules)

```bash
make setup        # Lock dependencies and install everything
make test         # Run all tests across workspace
make lint         # Format with ruff, type-check with mypy
make lint-check   # Check only (no fixes)
make pre-commit   # Run pre-commit hooks manually
make hooks        # Install pre-commit git hooks
make clean        # Remove all cache directories
```

### Submodule Level

Navigate to any `apps/*/` or `packages/*/` directory:

```bash
make test         # Run tests for this submodule only
make lint         # Lint this submodule only
```

**Run a single test:**
```bash
# From root or submodule directory
poetry run pytest path/to/test_file.py::test_function_name
poetry run pytest -k "test_pattern"
```

**Test discovery:** Tests are auto-discovered in `tests/` directories. No pytest.ini or conftest.py needed.

### REST API Development

**Start dev server:**
```bash
cd apps/rest_api
make start        # Starts uvicorn with hot-reload on http://0.0.0.0:8000
```

### Database Migrations (data_store)

```bash
cd packages/data_store

# Setup database first
docker compose up -d              # Start PostgreSQL + pgAdmin
sh ./scripts/setup_env.sh         # Generate .env from setup.env.sh

# Run migrations
make migrate-head                 # Upgrade to latest
make migrate-up                   # Upgrade one revision
make migrate-down                 # Downgrade one revision
make migrate-base                 # Downgrade to empty database (⚠️ destructive)

# Create new migration
make migrate-revision m="description"   # Auto-generate from schema changes
```

**Important:** Schema definitions must be imported in `/schema/__init__.py` for auto-detection.

## Key Conventions

### Adding Dependencies

**Always use `--directory` flag:**
```bash
poetry --directory apps/rest_api add <package>
poetry --directory packages/data_store add <package>
```

If packages get added to root `pyproject.toml`, you forgot the `--directory` flag. Remove them manually.

### Pre-commit Hooks

Hooks run automatically on commit:
- `ruff-format` - Code formatting
- `ruff-check --fix` - Linting with auto-fix
- `mypy` - Type checking (excludes `alembic/`, `migrations/`, and `conftest.py`)
- `pytest` - Full test suite (fails fast with `--maxfail=1`)

### Configuration Exclusions

- **mypy**: Excludes `alembic/` directories and `conftest.py` files
- **ruff**: Excludes `alembic/` directories in data_store
- Python version: **3.13** (strict requirement)

**Note:** conftest.py files are excluded from mypy because they are pytest-specific test configuration files that can have duplicate names across packages in a monorepo.

### Repository Provider Pattern

Don't instantiate repositories directly. Use providers:
```python
from data_store.repository.provider import get_locale_repository

repo = get_locale_repository()  # Returns LocaleRepoImpl instance
```

### FastAPI Application Factory

Don't import `app` directly. Use `create_app()` factory:
```python
from rest_api.start import create_app

app = create_app()  # Returns configured FastAPI instance
```

### Module Structure

Each app/package follows this structure:
```
module_name/
├── src/module_name/   # Source code with py.typed for type stubs
├── tests/             # Tests mirror src/ structure
├── conftest.py        # Shared test fixtures
├── pyproject.toml     # Module dependencies
├── makefile           # Includes ../../.makefile_base
└── README.md
```

## Testing

### Shared Test Fixtures

LocaleIQ provides comprehensive test fixtures via `conftest.py` files at root and module levels.

**REST API fixtures** (`apps/rest_api/conftest.py`):
- `test_client` - FastAPI TestClient for integration tests
- `fake_clock` - Deterministic clock (fixed at 2025-11-15T10:23:00 UTC)
- `utc_time` - Fixed UTC datetime
- `sample_timezones` - Common timezone list

**Data Store fixtures** (`packages/data_store/conftest.py`):
- `mock_db_session` - Mock database session for unit tests
- `test_db_url` - Test database URL (from `TEST_DB_URL` env var)
- `sample_locale_data` - Sample locale data

**Utils fixtures** (`packages/utils/conftest.py`):
- `temp_env_file` - Temporary .env file
- `clean_env` - Saves/restores environment variables

### Test Patterns

- Use `fake_clock` fixture instead of creating FakeClock instances
- Use `test_client` fixture for API tests
- Repository tests: use `mock_db_session` for unit tests
- Add docstrings to complex tests

See [TESTING.md](../TESTING.md) for complete guide.

## Relevant Files

- `.makefile_base` - Shared makefile included by all submodules
- `.pre-commit-config.yaml` - Pre-commit hook definitions
- `HOWTO.md` - Dependency management instructions
- `TESTING.md` - Comprehensive testing guide
