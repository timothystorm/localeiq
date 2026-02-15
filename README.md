# LocaleIQ

A FastAPI-based REST API providing chronology, time, timezone, and locale management services. Built as a Python Poetry monorepo with strict module isolation.

## 🚀 Quick Start

### Prerequisites

- Python 3.13
- Poetry 2.2.1+
- Docker & Docker Compose (for database)

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd localeiq

# Set up the workspace (installs all dependencies)
make setup

# Activate virtual environment
poetry shell
```

### Running the API

```bash
# Start the development server
cd apps/rest_api
make start

# API will be available at http://localhost:8000
# Interactive docs at http://localhost:8000/docs
```

### Running Tests

```bash
# Run all tests
make test

# Run tests for a specific module
cd apps/rest_api && make test
cd packages/data_store && make test

# Run a specific test
poetry run pytest path/to/test_file.py::test_name
```

## 📁 Project Structure

LocaleIQ uses a **monorepo architecture** with Poetry workspace management:

```
localeiq/
├── apps/                  # Standalone applications
│   ├── rest_api/         # FastAPI REST API service
│   └── cli_tool/         # Command-line interface
├── packages/             # Shared libraries
│   ├── data_store/       # Database layer (PostgreSQL, Alembic)
│   └── utils/            # Common utilities
└── pyproject.toml        # Root config (editor integration only)
```

### Key Principles

- **Each submodule is independent** with its own `pyproject.toml`
- **Root `pyproject.toml`** is for editor integration only (NO runtime dependencies)
- **Shared `poetry.lock`** at root ensures consistent dependency versions
- **Shared makefiles** via `.makefile_base` for consistent commands

## 🏗️ Architecture

### Layer Design

```
┌─────────────────────────────────────┐
│  REST API (FastAPI)                 │
│  ├── Routers (HTTP endpoints)       │
│  ├── Services (Business logic)      │
│  └── DTOs (Data transfer objects)   │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│  Data Store (PostgreSQL)            │
│  ├── Repositories (Interfaces)      │
│  ├── Implementations (SQL)          │
│  └── Schemas (SQLAlchemy models)    │
└─────────────────────────────────────┘
```

**Key Patterns:**
- **Repository Pattern**: Abstract data access via interfaces (`locale_repo.py` → `locale_repo_impl.py`)
- **Provider Functions**: Factory functions for dependency injection (`get_locale_repository()`)
- **Application Factory**: FastAPI app created via `create_app()` function

## 🛠️ Development

### Available Commands

```bash
make help         # Show all available commands
make setup        # Initial setup (lock + install + hooks)
make test         # Run all tests
make lint         # Format and lint code
make lint-check   # Check code without fixing
make pre-commit   # Run pre-commit hooks manually
make clean        # Remove cache directories
```

### Adding Dependencies

**Always use `--directory` flag** to add dependencies to the correct submodule:

```bash
# ✅ Correct
poetry --directory apps/rest_api add httpx

# ❌ Wrong (adds to root pyproject.toml)
poetry add httpx
```

See [HOWTO.md](./HOWTO.md) for more details.

### Database Setup

The data_store package includes PostgreSQL database with Alembic migrations:

```bash
cd packages/data_store

# 1. Create environment file
cp .env.local .env
# Edit .env with your database credentials

# 2. Start database services
docker compose up -d

# 3. Run migrations
make migrate-head

# Access:
# - PostgreSQL: localhost:5432
# - pgAdmin: http://localhost:8080
```

**Migration commands:**
```bash
make migrate-revision m="add user table"  # Create new migration
make migrate-up                           # Apply one migration
make migrate-down                         # Rollback one migration
make migrate-head                         # Apply all migrations
```

### Code Quality

Pre-commit hooks automatically run on every commit:
- **ruff** - Code formatting and linting
- **mypy** - Static type checking
- **pytest** - Full test suite

```bash
# Install hooks (included in make setup)
make hooks

# Run manually
make pre-commit
```

## 📚 Documentation

- [HOWTO.md](./HOWTO.md) - Dependency management guide
- [.github/copilot-instructions.md](./.github/copilot-instructions.md) - AI assistant development guide
- [apps/rest_api/README.md](./apps/rest_api/README.md) - REST API documentation
- [packages/data_store/README.md](./packages/data_store/README.md) - Database setup guide

## 🧪 Testing

Tests are organized to mirror the source structure:

```
rest_api/
├── src/rest_api/
│   ├── api/
│   ├── service/
│   └── dto/
└── tests/
    ├── api/          # API integration tests
    └── service/      # Service unit tests
```

**Test patterns:**
- Use `FakeClock` for time-dependent tests
- Repository tests use shared fixtures from `conftest.py`
- API tests use FastAPI `TestClient` with shared fixtures

## 🤝 Contributing

1. Create a feature branch from `main`
2. Make your changes following existing patterns
3. Ensure tests pass: `make test`
4. Ensure linting passes: `make lint-check`
5. Commit (pre-commit hooks will run automatically)
6. Submit a pull request

## 📄 License

[Add your license here]

## 📧 Contact

Timothy Storm - timothystorm@gmail.com
