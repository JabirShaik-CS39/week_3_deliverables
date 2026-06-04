from sqlalchemy import Table, Column, Integer, ForeignKey,String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship,Base

# Association Table (NO class needed)
student_course = Table(
    "student_course",
    Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True),
)


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    courses: Mapped[list["Course"]] = relationship(
        secondary=student_course,
        back_populates="students"
    )


class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))

    students: Mapped[list["Student"]] = relationship(
        secondary=student_course,
        back_populates="courses"
    )