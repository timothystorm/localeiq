import os

import uvicorn

"""
Production server entry point for LocaleIQ application.
"""

UVICORN_RELOAD = os.getenv("UVICORN_RELOAD", "False").lower() in ("true", "1")
UVICORN_HOST = os.getenv("UVICORN_HOST", "0.0.0.0")
UVICORN_PORT = int(os.getenv("UVICORN_PORT", "8000"))

def start():
    """
    Start the LocaleIQ application server using Uvicorn.

    Environment variables:
    ----------
    UVICORN_RELOAD : False
        Enable auto-reload
    UVICORN_HOST : 0.0.0
        Host address to bind
    UVICORN_PORT :  8000
        Port number to bind
    """
    uvicorn.run("localeiq.main:app", host=UVICORN_HOST, port=UVICORN_PORT, reload=UVICORN_RELOAD)

if __name__ == "__main__":
    start()