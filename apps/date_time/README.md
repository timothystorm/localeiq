# LocaleIQ - Date & Time Application

The Date & Time application provides users with tools to manage and manipulate date and time data effectively. It
includes features for formatting, parsing, and converting date and time values across different time zones and locales.

## Start the Application
To start the Date & Time application, run the following command in your terminal:

```bash
   poetry run uvicorn date_time.main:app --reload --host 0.0.0.0 --port 8000
```

## Endpoints

- **/v1/time**: Return the current time in the specified timezone.
```bash
   curl -X GET http://0.0.0.0:8000/v1/time?tz=America/Denver -H "Content-Type: application/json"
```