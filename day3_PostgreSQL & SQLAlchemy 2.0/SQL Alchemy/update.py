from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import psycopg2

engine = create_engine(
    "postgresql://postgres:Welcome%402826@localhost:5432/fastapi_db"
)

Base = declarative_base()

class Admin(Base):
    __tablename__ = "Admin"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Session = sessionmaker(bind=engine)
session = Session()

# Get row with id=1
admin = session.query(Admin).filter_by(id=1).first()

if admin:
    admin.name = "Updated Name"
    admin.age = 40

    session.commit()
    print("Record updated successfully")
else:
    print("Record not found")