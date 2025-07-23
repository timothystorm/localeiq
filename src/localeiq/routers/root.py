from fastapi import APIRouter

from localeiq.models.root_context import RootContext

router = APIRouter()


@router.get("/")
def root():
    """
    Returns the welcome statement for the LocaleIQ API and MCP (Model Context Provider).
    """
    return RootContext(
        name="LocaleIQ API",
        version="1.0.0",
        description="Provides internationalization and geographic boundary data.",
        endpoints=["/countries", "/countries/count", "/regions/{postal}"],
    )
