import importlib
import inspect
import pathlib
import pkgutil
from contextlib import asynccontextmanager

from fastapi import FastAPI, APIRouter


def load_routers(_app: FastAPI, package: str = "localeiq.routers"):
    """
    Dynamically find and register all APIRouter instances in the given package
    """
    package_path = pathlib.Path(__file__).parent / "routers"

    for module_info in pkgutil.walk_packages(
        path=[str(package_path)],
        prefix=f"{package}.",
        onerror=lambda x: None,
    ):
        module_name = module_info.name

        # Dynamically import module
        module = importlib.import_module(module_name)

        # Look for a router variable in the module
        for name, obj in inspect.getmembers(module):
            if isinstance(obj, APIRouter) and name == "router":
                app.include_router(obj)
                print(f"📝 Registered: {module_name}")


@asynccontextmanager
async def lifespan(_app: FastAPI):
    load_routers(app)
    for route in app.routes:
        print(f"✅ {getattr(route, 'name')} → {getattr(route, 'path')}")
    yield  # Application runs here


"""
Main entry point for the LocaleIQ API.
"""
app = FastAPI(
    title="LocaleIQ API",
    description="System for fetching locale information",
    version="1.0.0",
    lifespan=lifespan,
)
