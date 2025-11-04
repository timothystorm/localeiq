import os

from fastapi import FastAPI

from localeiq.routers import country

"""
Main entry point for LocaleIQ API.
"""

app = FastAPI()
app.include_router(country.router)


@app.get("/")
def read_root():
    return {"hello": "world"}