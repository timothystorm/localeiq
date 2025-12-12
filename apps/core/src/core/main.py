import uvicorn
from fastapi import FastAPI

from core.api.middleware.timer_middleware import TimerMiddleware
from core.api.middleware.tracer_middleware import TracerMiddleware
from core.api.router.chrono.chrono_router import router as time_router


def create_app() -> FastAPI:
    core_app = FastAPI(title="LocaleIQ Chronology and Time API", version="1.0.0")

    # Include routers
    core_app.include_router(time_router)

    # Add middleware
    core_app.add_middleware(TracerMiddleware)
    core_app.add_middleware(TimerMiddleware)
    return core_app


app = create_app()

if __name__ == "__main__":
    """
    Development server entry point. Do NOT use in production.
    """
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="debug")
