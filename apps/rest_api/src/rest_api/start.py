import uvicorn
from fastapi import FastAPI

from rest_api.api.middleware.timer_middleware import TimerMiddleware
from rest_api.api.middleware.tracer_middleware import TracerMiddleware
from rest_api.api.router.chrono.time_router import router as time_router
from rest_api.api.router.chrono.timezone_router import router as timezone_router
from rest_api.api.router.locale.locale_router import router as locale_router


def create_app() -> FastAPI:
    rest_api = FastAPI(
        title="LocaleIQ chronology, time, and timezone API", version="1.0.0"
    )

    # Include chrono routers
    rest_api.include_router(time_router)
    rest_api.include_router(timezone_router)

    # Include locale routers
    rest_api.include_router(locale_router)

    # Add middleware
    rest_api.add_middleware(TracerMiddleware)
    rest_api.add_middleware(TimerMiddleware)
    return rest_api


app = create_app()

if __name__ == "__main__":
    """
    Development server entry point. Do NOT use in production.
    """
    uvicorn.run("start:app", host="0.0.0.0", port=8000, reload=True, log_level="debug")
