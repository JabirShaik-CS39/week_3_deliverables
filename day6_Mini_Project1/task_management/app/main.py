from fastapi import FastAPI
from app.routers import auth, users, projects, tasks

app = FastAPI(title="Task Management API", version="0.1.0")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(projects.router, prefix="/projects", tags=["projects"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Task Management API is running"}
