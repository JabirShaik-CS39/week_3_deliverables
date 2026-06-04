# creation of data table and insertion of records into the Admin table using SQLAlchemy

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Admins(Base):
    __tablename__ = "Admin"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

engine = create_engine(
    "postgresql://postgres:Welcome%402826@localhost:5432/fastapi_db"
)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
s = Session()

Admins = [
    Admins(name="Jani", age=32),
    Admins(name="mahesh", age=35),
    Admins(name="charan", age=15)
]

s.add_all(Admins)
s.commit()

print("Admins inserted successfully")
