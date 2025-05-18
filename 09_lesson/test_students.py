from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "postgresql://postgres:1234@localhost:5432/qa_utf8"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


def test_add_student():
    session = Session()
    student = Student(name="Test Student", age=21)
    session.add(student)
    session.commit()

    added = session.query(Student).filter_by(
        name="Test Student", age=21
    ).first()
    assert added is not None

    session.delete(added)
    session.commit()
    session.close()


def test_update_student():
    session = Session()
    student = Student(name="Update Student", age=18)
    session.add(student)
    session.commit()

    student.age = 25
    session.commit()

    updated = session.query(Student).filter_by(name="Update Student").first()
    assert updated.age == 25

    session.delete(updated)
    session.commit()
    session.close()


def test_delete_student():
    session = Session()
    student = Student(name="Delete Student", age=30)
    session.add(student)
    session.commit()

    session.delete(student)
    session.commit()

    deleted = session.query(Student).filter_by(name="Delete Student").first()
    assert deleted is None

    session.close()
