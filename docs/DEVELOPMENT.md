# Development Guide

Welcome to the LocaleIQ monorepo.
This guide explains how to set up the development environment, run tests, lint code, and understand the project structure.

This assumes:
- macOS or Linux
- Python 3.14
- Poetry 2.2.x
- Make installed
- Git installed

---

### 1. Clone Repository

```bash
git clone git@github.com:timothystorm/localeiq.git
cd localeiq
```

> (SSH recommended.)

### 2. Install Prerequisites

**Python 3.14 + pyenv**

Install pyenv and then:
```bash
pyenv install 3.14.0
pyenv local 3.14.0
```

**Poetry 2.2.x**
```bash
pip install --upgrade pip
pip install poetry==2.2.1
```

*Ensure Poetry uses a project-level venv:*
```bash
poetry config virtualenvs.in-project true
```

---

### 3. Run the Unified Setup

All developer initialization is centralized in the Makefile.
```bash
make setup
```

This will:
- create .venv
- install all dependencies
- install dev tooling (pytest, black, isort, mypy, etc.)
- install pre-commit hooks

---

### 4. Activate the Virtualenv (optional)

Poetry manages this automatically, but you may activate manually:
```bash
source .venv/bin/activate
```

### 5. Project Structure Overview

```text
localeiq/
  shared/        ← reusable cross-domain utilities
  data/          ← ingestion, parsing, enrichment
  datetime/
  language/
  culture/
  geopolitical/
  economic/
  docs/
  .venv/
  pyproject.toml
  pytest.ini
  Makefile
```

> Rule: Modules may import shared or data, but may not import each other.

---

### 6. Running Tests

Run full suite (parallel using xdist):
```bash
make test
```

Run tests per module:
```bash
make test-module MODULE=language
make test-module MODULE=date_time
```

Run all modules in parallel:
```bash
make test-all
```

---

### 7. Linting & Formatting

Run full lint (ruff/isort/mypy):
```bash
make lint
```

Run code format (black/isort):
```bash
make format
```

Pre-commit checks manually:
```bash
poetry run pre-commit run --all-files
```

---

### 8. Adding a New Module

1.	Create the directory:
  ```text
  {new_module}/
    src/{new_module}/
    tests/
  ```
2. Add the module to:
- matrix CI 
- Makefile MODULES list 
- pyproject references (if needed)
3.	Ensure it imports only from shared or data.

---

### 9. Running a Single Test or Debugging

```bash
# from the repo root
poetry run pytest date_time/tests/test_placeholder.py::test_answer_to_everything -vv
```

---

### 10. Coding Rules & Standards

- Use snake_case for variables & functions
- Use PascalCase for classes
- Keep API schemas shallow (≤ 3 levels)
- Include a minimal meta block in all API responses
- Avoid abbreviations unless globally standardized (ISO codes, CLDR, etc.)
- Write unit tests for every module
- Use shared config and logging tools (never duplicate them)

---

### 11. Updating Dependencies

```bash
poetry update
make setup
make test
```

--- 

### 12. Type Checking

```bash
make type-check
```

---

### 13. Git Etiquette

- Never commit failing tests
- Never commit without pre-commit passing
- Create focused branches per feature
- Write clear commit messages
    - use [conventional commit messages](https://www.conventionalcommits.org/en/v1.0.0/)
- Keep PRs small and composable

---

### 14. Common Issues

❌ isort scanning .venv
→ Fixed via skip = [".venv"] in pyproject + pre-commit exclude.

❌ exit code 5 (no tests ran)
→ Add placeholder test per module.

❌ virtualenv not cached in CI
→ Ensure virtualenvs.in-project = true and never delete .venv in Make.

---

### 15. Before Submitting Code

```bash
make type-check
make format
make lint
make test
```
> (These run automatically in CI but should be run locally as well.)

---

