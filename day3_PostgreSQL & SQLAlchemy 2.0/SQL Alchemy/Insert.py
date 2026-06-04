# insertion of a record into the Admin table using SQLAlchemy

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Database Connection
engine = create_engine(
    "postgresql://postgres:Welcome%402826@localhost:5432/fastapi_db"
)

Base = declarative_base()

# Map Existing Table
class Admin(Base):
    __tablename__ = "Admin"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create Session
Session = sessionmaker(bind=engine)
session = Session()

# Insert One Record
new_admin = Admin(
    name="Jani",
    age=32
)

session.add(new_admin)
session.commit()

print("Record inserted successfully!")