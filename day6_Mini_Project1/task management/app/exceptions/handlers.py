from fastapi import Request
from fastapi import HTTPException

from fastapi.responses import (
    JSONResponse
)

from starlette import status


async def http_exception_handler(
    request: Request,
    exc: HTTPException
):

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.detail
        }
    )


async def generic_exception_handler(
    request: Request,
    exc: Exception
):

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "success": False,
            "message": "Internal Server Error"
        }
    )