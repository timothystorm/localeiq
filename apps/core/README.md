# LocaleIQ - Core Application

The core application provides users with tools to manage and manipulate locale data effectively. 

## Start the Application
To start the core application, run the following command in your terminal:

```bash
   poetry run uvicorn core.main:app --reload --host 0.0.0.0 --port 8000
```

## Endpoints

- **v1/time/now[?tz=timezone]**: Return the current time in the specified timezone.