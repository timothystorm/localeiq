import uvicorn
from fastapi import FastAPI

from date_time.api.middleware.timer_middleware import TimerMiddleware
from date_time.api.middleware.tracer_middleware import TracerMiddleware
from date_time.api.router.time_router import router as time_router


def create_app() -> FastAPI:
    date_time_app = FastAPI(title="LocaleIQ DateTime API", version="1.0.0")

    # Include routers
    date_time_app.include_router(time_router)

    # Add middleware
    date_time_app.add_middleware(TracerMiddleware)
    date_time_app.add_middleware(TimerMiddleware)
    return date_time_app


app = create_app()

if __name__ == "__main__":
    """
    Development server entry point. Do NOT use in production.
    """
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="debug")
