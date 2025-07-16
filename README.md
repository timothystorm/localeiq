# LocaleIQ

> Momentum beats motivation!

## Environment Setup

### Install poetry dependencies

Install poetry dependencies and add your `/src` directory and sets up the
virtual environment.

Needs to be run each time...

* the project is cloned
* a new dependency is added

```bash
poetry install
```

## Endpoints

### Countries

Fetch countries list...

```GET: /countries```

## Execute

Run the uvicorn server...
``
```bash
poetry run uvicorn localeiq.main:app --reload
```

Here’s the answer formatted in **wiki/markdown-friendly style** for your `TODO.md` or internal docs:

---

## 🗂️ FastAPI Project Structure for LocaleIQ (MVC-like Architecture)

This architecture separates concerns cleanly and scales well for LocaleIQ’s future needs.

---

### 📁 Recommended Directory Layout:

```
src/
└── localeiq/
    ├── main.py              # FastAPI app instance, includes routers
    ├── routers/             # Routers = Controllers (API layer)
    │   ├── countries.py     # Handles HTTP routes for countries
    │   └── root.py          # Other root-level endpoints
    ├── services/            # Business logic layer (Services)
    │   └── country_service.py
    ├── repositories/        # Data access layer (Repositories)
    │   └── country_repository.py
    ├── models/              # Pydantic schemas & ORM models
    │   └── country.py
    └── db/                  # DB configuration (optional)
        └── session.py       # For DB sessions or connections
```

---

### ✅ Purpose of Each Layer:

| Layer          | Folder          | Purpose                                            |
| -------------- | --------------- | -------------------------------------------------- |
| **Router**     | `routers/`      | API layer — receives requests, returns responses.  |
| **Service**    | `services/`     | Business logic, orchestration of lower layers.     |
| **Repository** | `repositories/` | Direct DB or data source access (fetching data).   |
| **Model**      | `models/`       | Pydantic schemas & ORM models (DTOs, validations). |

---

### ✅ Typical Data Flow:

```
HTTP Request → Router → Service → Repository → Data Source (DB, JSON, etc.)
```

---

### ✅ Example Code:

#### `/routers/countries.py`

```python
from fastapi import APIRouter
from localeiq.services.country_service import CountryService

router = APIRouter()
country_service = CountryService()

@router.get("/countries")
def list_countries():
    return country_service.get_all_countries()
```

---

#### `/services/country_service.py`

```python
from localeiq.repositories.country_repository import CountryRepository

class CountryService:
    def __init__(self):
        self.repo = CountryRepository()

    def get_all_countries(self):
        return self.repo.fetch_countries()
```

---

#### `/repositories/country_repository.py`

```python
class CountryRepository:
    def fetch_countries(self):
        # Example static data (can be swapped with DB later)
        return [
            Country(code="US", name="United States"),
            Country(code="CA", name="Canada")
        ]
```

---

#### `/models/country.py`

```python
from pydantic import BaseModel

class Country(BaseModel):
    code: str
    name: str
```

---

#### `/main.py`

```python
from fastapi import FastAPI
from localeiq.routers import countries, root

app = FastAPI()
app.include_router(root.router)
app.include_router(countries.router)
```

---

### ✅ Advantages:

* Clear separation of concerns.
* Easy to swap JSON with a database later by replacing only the repository layer.
* Router layer stays clean and focused on HTTP details.
* Scales well for future features like states, cities, boundaries, etc.

---

### ✅ Suggested Next Steps:

* Scaffold this directory structure.
* Move existing country endpoints into this layered structure.
* Future: Add database integration via the repository layer.

---

Let me know if you want me to generate a ready-to-commit version of this structure!

## Data Sources

Unicode Common Locale Data Repository - https://github.com/unicode-org/cldr-json

## Credits

This project includes data derived from the Unicode Common Locale Data Repository (CLDR).

© Unicode, Inc. All rights reserved.
Unicode data files are provided “as-is” without warranty of any kind.
Use of Unicode data is subject to the terms of the Unicode License Agreement:
https://www.unicode.org/license.html

If any modifications have been made to CLDR data, they are not endorsed by Unicode and may differ from the official CLDR
distributions.
