from sqlalchemy import Float, create_engine, Column, Integer, String, text
from sqlalchemy.orm import declarative_base, Session


engine = create_engine('sqlite+pysqlite:///:memory:', echo=True, future=True)
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    grade = Column(Float)

Base.metadata.create_all(engine)

with Session(engine) as session:
    new_user1 = Student(name="Jan Kowalski", age=20, grade=5.5)
    new_user2 = Student(name="Maciej Wasilewski", age=25, grade=4.7)
    new_user3 = Student(name="Robert Lewandowski", age=36, grade=5.0)

    session.add_all([new_user1, new_user2, new_user3])

    session.commit()

with Session(engine) as session:
    students = session.execute(text("SELECT * FROM students")).all()
    for user in students:
        print(f'{user.name}, {user.age}, {user.grade}')