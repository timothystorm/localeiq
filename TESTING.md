# Testing Guide

This document describes the testing infrastructure and best practices for LocaleIQ.

## Test Structure

Tests are organized to mirror the source code structure:

```
module/
├── src/module_name/
│   ├── api/
│   ├── service/
│   └── repository/
└── tests/
    ├── api/          # Integration tests for API endpoints
    ├── service/      # Unit tests for business logic
    └── repository/   # Tests for data access layer
```

## Running Tests

### All Tests

```bash
# From workspace root
make test

# From specific module
cd apps/rest_api && make test
cd packages/data_store && make test
```

### Single Test or Pattern

```bash
# Run specific test file
poetry run pytest tests/service/chrono/time_service_test.py

# Run specific test function
poetry run pytest tests/service/chrono/time_service_test.py::TestNow::test_now

# Run tests matching pattern
poetry run pytest -k "test_now"
```

### Parallel Execution

```bash
# Run tests in parallel (requires pytest-xdist)
poetry run pytest -n auto
```

## Shared Fixtures

### Root-Level Fixtures (`conftest.py`)

Available to all tests across the workspace:

```python
def test_with_data_dir(test_data_dir):
    """test_data_dir provides path to test data directory."""
    data_file = test_data_dir / "sample.json"
```

### REST API Fixtures (`apps/rest_api/conftest.py`)

#### `test_client`
FastAPI TestClient for API integration tests:

```python
def test_get_time_endpoint(test_client):
    response = test_client.get("/v1/time/now?tz=UTC")
    assert response.status_code == 200
    assert "iso_8601" in response.json()
```

#### `fake_clock`
Fake clock for deterministic time-based testing:

```python
def test_service_with_fixed_time(fake_clock):
    service = TimeService(clock=fake_clock)
    result = service.now("America/Denver")
    assert result.to_iso8601_string() == "2025-11-15T03:23:00-07:00"
```

#### `utc_time`
Fixed UTC datetime for consistent testing:

```python
def test_with_fixed_utc(utc_time):
    assert utc_time.timezone_name == "UTC"
    assert utc_time.year == 2025
```

#### `sample_timezones`
List of commonly tested timezones:

```python
def test_all_timezones(sample_timezones):
    for tz in sample_timezones:
        # Test with UTC, America/Denver, etc.
        pass
```

### Data Store Fixtures (`packages/data_store/conftest.py`)

#### `mock_db_session`
Mock database session for unit tests:

```python
def test_repository_without_db(mock_db_session):
    repo = LocaleRepoImpl(session=mock_db_session)
    # Test repository logic without real database
```

#### `test_db_url`
Test database URL (override with `TEST_DB_URL` env var):

```python
def test_with_real_db(test_db_url):
    engine = create_engine(test_db_url)
    # Use real test database
```

#### `sample_locale_data`
Sample locale data for testing:

```python
def test_locale_creation(sample_locale_data):
    locale = Locale(**sample_locale_data)
    assert locale.locale_code == "en_US"
```

### Utils Fixtures (`packages/utils/conftest.py`)

#### `temp_env_file`
Temporary .env file for config testing:

```python
def test_config_loading(temp_env_file):
    temp_env_file.write_text("KEY=value\nDEBUG=true")
    config = load_config(temp_env_file)
    assert config.KEY == "value"
```

#### `clean_env`
Saves and restores environment variables:

```python
def test_env_dependent_code(clean_env):
    os.environ["TEST_VAR"] = "test_value"
    # Test code that reads TEST_VAR
    # Environment automatically restored after test
```

## Writing Tests

### Best Practices

1. **One assertion per test** (when possible) for clear failure messages
2. **Use descriptive test names** that explain what is being tested
3. **Use fixtures** to reduce duplication and improve readability
4. **Add docstrings** to complex tests explaining the scenario

### Example Test Structure

```python
from rest_api.service.chrono.chrono_service import TimeService


class TestTimeService:
    """Tests for TimeService time conversion functionality."""

    def test_convert_utc_to_denver(self, fake_clock):
        """Test converting UTC time to Denver timezone."""
        service = TimeService(clock=fake_clock)
        
        result = service.convert(
            "2025-11-15T10:23:00",
            from_tz="UTC",
            to_tz="America/Denver"
        )
        
        assert result.timezone_name == "America/Denver"
        assert result.to_iso8601_string() == "2025-11-15T03:23:00-07:00"

    def test_convert_invalid_timezone_raises_error(self, fake_clock):
        """Test that invalid timezone raises appropriate error."""
        service = TimeService(clock=fake_clock)
        
        with pytest.raises(Exception) as exc_info:
            service.convert(
                "2025-11-15T10:23:00",
                from_tz="INVALID/TZ",
                to_tz="UTC"
            )
        
        assert "Invalid timezone" in str(exc_info.value)
```

### API Integration Tests

```python
def test_get_current_time_endpoint(test_client):
    """Test /v1/time/now endpoint returns current time."""
    response = test_client.get("/v1/time/now?tz=America/Denver")
    
    assert response.status_code == 200
    data = response.json()
    assert "iso_8601" in data
    assert "tz" in data
    assert data["tz"] == "America/Denver"


def test_invalid_timezone_returns_400(test_client):
    """Test endpoint returns 400 for invalid timezone."""
    response = test_client.get("/v1/time/now?tz=INVALID")
    
    assert response.status_code == 400
    assert "detail" in response.json()
```

## Database Testing

### Setup Test Database

Set the `TEST_DB_URL` environment variable:

```bash
export TEST_DB_URL="postgresql+psycopg2://test_user:test_pass@localhost:5432/localeiq_test"
```

### Repository Tests

```python
def test_repository_logic_without_db(mock_db_session):
    """Test repository logic with mock session."""
    repo = LocaleRepoImpl(session=mock_db_session)
    # Test without hitting real database


def test_repository_with_real_db(test_db_url):
    """Integration test with real database."""
    # Setup test data
    # Run test
    # Cleanup
```

## Continuous Integration

Tests run automatically on every push via GitHub Actions (`.github/workflows/ci.yml`):

1. Lint check (ruff, mypy)
2. Full test suite
3. Pre-commit hooks validation

### Local Pre-commit

Before pushing, run pre-commit checks locally:

```bash
make pre-commit
```

This runs:
- Code formatting (ruff format)
- Linting (ruff check)
- Type checking (mypy)
- Full test suite

## Troubleshooting

### Tests Not Discovered

Ensure test files follow pytest conventions:
- Named `test_*.py` or `*_test.py`
- Test functions start with `test_`
- Test classes start with `Test` (no `__init__` method)

### Import Errors

Check that `PYTHONPATH` includes the correct `src/` directories. This is automatically configured in:
- Root `pyproject.toml` (for local development)
- `.github/workflows/ci.yml` (for CI)

### Mypy Duplicate Module Errors

In monorepos with multiple `conftest.py` files, mypy may complain about duplicate modules. This is fixed by excluding conftest files from type checking:

```toml
[tool.mypy]
exclude = [
    "^alembic/",
    ".*/conftest\\.py$"
]
```

This is configured in both root and submodule `pyproject.toml` files. conftest.py files don't need type checking since they're pytest-specific configuration.

### Fixture Not Found

Ensure `conftest.py` is in the correct location:
- Root `conftest.py` - Available to all tests
- Module `conftest.py` - Available to that module's tests only

### Database Connection Issues

For database integration tests:
1. Ensure PostgreSQL is running: `docker compose up -d`
2. Set `TEST_DB_URL` environment variable
3. Run migrations on test database: `make migrate-head`

## Further Reading

- [pytest documentation](https://docs.pytest.org/)
- [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [Testing best practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html)
