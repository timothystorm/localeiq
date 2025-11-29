import json
import time

import pendulum
from starlette.concurrency import iterate_in_threadpool
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response


class MetaMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response: Response = await call_next(request)

        if "application/json" in response.headers.get("content-type", ""):
            response_body = [chunk async for chunk in response.body_iterator]
            original_body = b"".join(response_body).decode()

            try:
                body = json.loads(original_body)
                new_body = { "data": body }

                # include meta if requested
                if request.headers.get("x-meta"):
                    new_body["_meta"] = {
                        "input_params": dict(**request.query_params),
                        "request_ts": pendulum.now("UTC").to_iso8601_string()
                    }

                modified_body = json.dumps(new_body).encode()
                response.headers["content-length"] = str(len(modified_body))
                response.body_iterator = iterate_in_threadpool(iter([modified_body]))
            except json.JSONDecodeError:
                pass # just emit the original response

        return response
