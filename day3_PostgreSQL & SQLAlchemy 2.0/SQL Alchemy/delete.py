# Delete a record from the Admin table using SQLAlchemy

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

# Delete Record with id = 4
admin_to_delete = session.query(Admin).filter_by(id=4).first()

if admin_to_delete:
    session.delete(admin_to_delete)
    session.commit()

    print("Record deleted successfully!")
else:
    print("Record not found!")



