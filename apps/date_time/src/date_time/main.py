from fastapi import FastAPI

from date_time.api.time_router import router as time_router


def create_app() -> FastAPI:
    date_time_app = FastAPI(title="LocaleIQ DateTime API", version="1.0.0")
    date_time_app.include_router(time_router)
    return date_time_app


app = create_app()
