from fastapi import FastAPI

from .routers import countries, root, regions

app = FastAPI(
    title="LocaleIQ API",
    description="System for fetching locale information",
    version="1.0.0",
)
app.include_router(root.router)
app.include_router(countries.router)
app.include_router(regions.router)
