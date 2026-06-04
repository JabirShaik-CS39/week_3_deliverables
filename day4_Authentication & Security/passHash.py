from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

password = "Welcome@123"

hashed_password = pwd_context.hash(password)

print("Hash:", hashed_password)

print(
    pwd_context.verify(
        "Welcome@123",
        hashed_password
    )
)



# creation of data table and insertion of records into the Admin table using SQLAlchemy

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)
Base = declarative_base()

class Login(Base):
    __tablename__ = "Login"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    Password = Column(String)

engine = create_engine(
    "postgresql://postgres:Welcome%402826@localhost:5432/fastapi_db"
)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
s = Session()

Logins = [
    Login(email="jani@example.com", Password=pwd_context.hash("hashed_password_1")),
    Login(email="mahesh@example.com", Password=pwd_context.hash("hashed_password_2"))
   
]

s.add_all(Logins)
s.commit()

print("Logins inserted successfully")
