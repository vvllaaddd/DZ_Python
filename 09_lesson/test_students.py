import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


# Настройки подключения к БД
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/qa_utf8"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()


# Модель таблицы
class Student(Base):
    __tablename__ = 'student'

    user_id = Column(Integer, primary_key=True)
    level = Column(String)
    education_form = Column(String)
    subject_id = Column(Integer)


# Фикстура для создания сессии
@pytest.fixture
def session():
    session = Session()
    yield session
    session.close()


# Тест на добавление студента
def test_add_student(session):
    student = Student(
        user_id=999999,
        level="Intermediate",
        education_form="group",
        subject_id=1
    )
    session.add(student)
    session.commit()

    added = session.query(Student).filter_by(user_id=999999).first()
    assert added is not None
    assert added.level == "Intermediate"
    assert added.education_form == "group"

    session.delete(added)
    session.commit()


# Тест на обновление студента
def test_update_student(session):
    student = Student(
        user_id=999998,
        level="Beginner",
        education_form="personal",
        subject_id=1
    )
    session.add(student)
    session.commit()

    student.level = "Advanced"
    session.commit()

    updated = session.query(Student).filter_by(user_id=999998).first()
    assert updated.level == "Advanced"

    session.delete(updated)
    session.commit()


# Тест на удаление студента
def test_delete_student(session):
    student = Student(
        user_id=999997,
        level="Elementary",
        education_form="group",
        subject_id=1
    )
    session.add(student)
    session.commit()

    session.delete(student)
    session.commit()

    deleted = session.query(Student).filter_by(user_id=999997).first()
    assert deleted is None
