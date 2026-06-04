# creation of data table and insertion of records into the Admin table using SQLAlchemy

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

engine = create_engine(
    "postgresql://postgres:Welcome%402826@localhost:5432/fastapi_db"
)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
s = Session()

Users = [
    Users(name="Jani", age=32),
    Users(name="mahesh", age=35),
    Users(name="charan", age=15)
]

s.add_all(Users)
s.commit()

print("Users inserted successfully")
