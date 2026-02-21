# LocaleIQ

A FastAPI-based REST API providing chronology, time, timezone, and locale management services. Built as a Python Poetry monorepo with strict module isolation.

## 🚀 Quick Start

### Prerequisites

- Python 3.13
- Poetry 2.2.1+
- Docker & Docker Compose (for database)
- **Optional but recommended**: [just](https://github.com/casey/just) task runner (`brew install just`)

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd localeiq

# Setup (installs dependencies, pre-commit hooks)
just setup

# Activate virtual environment
poetry shell
```

### Running the API

```bash
# Start development server
just dev

# API will be available at http://localhost:8000
# Interactive docs at http://localhost:8000/docs
```

### Running Tests

```bash
# Run all tests
just test

# Run with coverage report
just test-cov

# Run in parallel (faster)
just test-parallel

# Run tests matching a pattern
just test-match "test_now"

# Test a specific module
just test-module apps/rest_api
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
├── justfile              # Development task runner
└── makefile              # CI-only commands
```

### Key Principles

- **Each submodule is independent** with its own `pyproject.toml`
- **Root `pyproject.toml`** is for editor integration only (NO runtime dependencies)
- **Shared `poetry.lock`** at root ensures consistent dependency versions
- **`justfile`** for all development tasks (fast, user-friendly)
- **`makefile`** for CI automation only (minimal, stable)

## 🛠️ Development

### Task Runners: Just for Dev, Make for CI

**Philosophy**: 
- 🛠️ **`just`** - All development commands (fast, user-friendly, feature-rich)
- ⚙️ **`make`** - CI-only commands (minimal, stable, widely available)

This gives you the best developer experience while keeping CI simple.

### Development Commands (just)

```bash
# See all available commands
just

# Common tasks
just setup        # Initial project setup
just dev          # Start development server
just test         # Run tests
just test-cov     # Tests with coverage report
just test-parallel # Faster parallel test execution
just lint         # Format and lint code
just db-up        # Start database
just db-migrate   # Run migrations
just clean        # Clean cache files

# Full list: just --list
```

### CI Commands (make)

**Note**: These are for CI automation. Use `just` for development.

```bash
make setup        # Install dependencies (CI uses this)
make lint-check   # Check code quality (CI uses this)
make test         # Run tests (CI uses this)
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
# Start database
just db-up

# Run migrations
just db-migrate

# Create new migration
just db-new-migration "add user table"

# Rollback last migration
just db-rollback

# View logs
just db-logs

# Stop database
just db-down
```

**Environment setup:**
```bash
cd packages/data_store
cp .env.local .env
# Edit .env with your database credentials
```

**Access:**
- PostgreSQL: `localhost:5432`
- pgAdmin: `http://localhost:8080`

### Code Quality

Pre-commit hooks automatically run on every commit:
- **ruff** - Code formatting and linting
- **mypy** - Static type checking
- ~~**pytest**~~ - Removed from pre-commit (run via `just test` or CI)

```bash
# Install hooks (included in just setup)
just hooks

# Run manually
just pre-commit
```

**Note:** Tests are no longer run on every commit for better developer experience. Run `just test` before pushing or rely on CI.

## 🧪 Testing

### Test Execution

```bash
# Quick test runs
just test                 # All tests
just test-parallel        # Parallel execution (faster)
just test-module apps/rest_api  # Single module
just test-match "test_now"      # Pattern matching

# With coverage
just test-cov             # Terminal + HTML report
```

### CI Testing

Our CI pipeline tests on **Python 3.13** (the deployment version):

- **Lint job**: Code quality checks (ruff, mypy)
- **Test job**: Full test suite on Python 3.13
- **Caching**: Dependencies cached for faster runs (~10-15s setup vs 2-3min)

**Why only 3.13?** We control deployment via Docker and pin Python 3.13. No need to test versions we don't deploy.

### Test Structure

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

See [TESTING.md](./TESTING.md) for comprehensive testing guide.

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
- **Dependency Injection**: FastAPI `Depends()` for proper lifecycle management
- **Application Factory**: FastAPI app created via `create_app()` function

## 📚 Documentation

- [HOWTO.md](./HOWTO.md) - Dependency management guide
- [TESTING.md](./TESTING.md) - Comprehensive testing guide
- [.github/copilot-instructions.md](./.github/copilot-instructions.md) - AI assistant development guide
- [apps/rest_api/README.md](./apps/rest_api/README.md) - REST API documentation
- [packages/data_store/README.md](./packages/data_store/README.md) - Database setup guide

## 🤝 Contributing

1. Create a feature branch from `main`
2. Make your changes following existing patterns
3. Run quality checks: `just ci` (runs lint + test)
4. **Optional**: Get an AI-powered code review: `./ai/code_review.sh`
5. Commit (pre-commit hooks will run automatically)
6. Push and submit a pull request

### Pre-Commit Workflow

Pre-commit hooks run **fast checks only**:
- ✅ Code formatting (ruff format)
- ✅ Linting (ruff check)
- ✅ Type checking (mypy)

Tests are **NOT** run on commit - run them manually:
```bash
just test        # Before committing
just test-watch  # During development
just ci          # Full CI simulation (lint + test)
```

CI will run the full test suite on push.

## 📦 CI/CD

### GitHub Actions Workflow

- **Lint job**: Code quality checks (ruff, mypy)
- **Test job**: Full test suite on Python 3.13
- **Caching**: Poetry dependencies and pre-commit hooks cached
- **Fast feedback**: See failures in ~2-3 minutes (with cache)

**Why only Python 3.13?** We control deployment via Docker and pin Python 3.13. No need to test versions we don't deploy.

### Local CI Simulation

```bash
# Run the same checks as CI
just ci

# Or step by step
just lint-check
just test
```

## 📄 License

[Add your license here]

## 📧 Contact

Timothy Storm - timothystorm@gmail.com
