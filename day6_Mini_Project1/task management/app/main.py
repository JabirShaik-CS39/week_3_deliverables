from fastapi import FastAPI
from fastapi import HTTPException

from app.routers import auth
from app.routers import users
from app.routers import projects
from app.routers import tasks

from app.middleware.request_id import (
    RequestIDMiddleware
)

from app.middleware.request_logger import (
    RequestLoggerMiddleware
)

from app.exceptions.handlers import (
    http_exception_handler,
    generic_exception_handler
)


app = FastAPI(
    title="Task Management API"
)


app.add_middleware(
    RequestIDMiddleware
)

app.add_middleware(
    RequestLoggerMiddleware
)


app.add_exception_handler(
    HTTPException,
    http_exception_handler
)

app.add_exception_handler(
    Exception,
    generic_exception_handler
)


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(projects.router)
app.include_router(tasks.router)


@app.get("/")
async def root():

    return {
        "message": "Task Management API Running"
    }