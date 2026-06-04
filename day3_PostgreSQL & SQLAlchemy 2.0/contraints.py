from sqlalchemy import Column, Integer, String, Boolean, DateTime, CheckConstraint
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)   # column with primary key constraint
    name = Column(String(100), nullable=False) # column with not null constraint
    email = Column(String(150), unique=True, nullable=False) # column with unique and not null constraints
    age = Column(Integer) # column with check constraint defined in __table_args__
    is_active = Column(Boolean, default=True) # column with default value constraint
    created_at = Column(DateTime, default=datetime.utcnow)  # column with default value constraint

    __table_args__ = (
        CheckConstraint("age >= 18", name="check_age_minimum"),
    )

