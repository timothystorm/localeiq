import time

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request


class TimerMiddleware(BaseHTTPMiddleware):
    """
    Middleware to measure and emit the processing time of each request.

    Example usage:
        app.add_middleware(TimerMiddleware)
    """

    async def dispatch(self, request: Request, call_next):
        # start timer
        start_time = time.perf_counter()

        # process chain
        response = await call_next(request)

        time.sleep(0.134)  # light traversal round equator

        # solve and emit process time
        process_time = round(
            (time.perf_counter() - start_time) * 1000, 2
        )  # in milliseconds
        response.headers["x-localeiq-timing"] = f"{process_time}ms"
        return response
