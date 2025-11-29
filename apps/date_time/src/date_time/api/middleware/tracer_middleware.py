import uuid

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response


class TracerMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        # get or create trace id
        trace_id = request.headers.get("x-trace-id") or str(uuid.uuid4())

        # process chain
        response = await call_next(request)

        # attach trace id to response
        response.headers["x-localeiq-id"] = trace_id
        return response
