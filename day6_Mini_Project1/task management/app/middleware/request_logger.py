import time
import logging

from starlette.middleware.base import BaseHTTPMiddleware


logging.basicConfig(
    level=logging.INFO
)

logger = logging.getLogger(
    "task_manager"
)


class RequestLoggerMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next
    ):

        start_time = time.time()

        response = await call_next(
            request
        )

        process_time = (
            time.time() - start_time
        )

        logger.info(
            f"{request.method} "
            f"{request.url.path} "
            f"{response.status_code} "
            f"{process_time:.4f}s"
        )

        return response