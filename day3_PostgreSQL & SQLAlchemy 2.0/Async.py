# Create Async Engine
from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/fastapi_db"

engine = create_async_engine(
    DATABASE_URL,
    echo=True,          # logs SQL queries
    future=True
)

# Create Async Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

