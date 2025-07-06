# LocaleIQ

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
