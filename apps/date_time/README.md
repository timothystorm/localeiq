# LocaleIQ - Date & Time Application

The Date & Time application provides users with tools to manage and manipulate date and time data effectively. It
includes features for formatting, parsing, and converting date and time values across different time zones and locales.

## Endpoints

- **/v1/time**: Return the current time in the specified timezone.
```bash
   curl -X POST http://0.0.0.0:8081/v1/time -d '{"timezone":"America/Denver"}' -H "Content-Type: application/json"
```