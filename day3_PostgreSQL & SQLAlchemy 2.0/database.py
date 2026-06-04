from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# PostgreSQL URL (change username/password/db if needed)
DATABASE_URL = "postgresql://postgres:Welcome%402826@localhost:5432/fastapi_db"

# Create engine
engine = create_engine(DATABASE_URL)

# Create SessionLocal (this is what you are importing)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()