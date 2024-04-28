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

def addStudents():
    new_user1 = Student(id = 1, name="Jan Kowalski", age=20, grade=5.5)
    new_user2 = Student(id = 2, name="Maciej Maciejewski", age=25, grade=4.7)
    new_user3 = Student(id = 3, name="Robert Lewandowski", age=36, grade=5.0)

    addStudent(new_user1)
    addStudent(new_user2)
    addStudent(new_user3)

def addStudent(student):
    with Session(engine) as session:
        session.add(student)
        session.commit()

def getStudentById(id):
    with Session(engine) as session:
        rows = session.execute(text(f"SELECT * FROM students WHERE id = {id}")).all()
        return Student(name = rows[0].name, age = rows[0].age, grade = rows[0].grade)
    
def updateStudentById(id, name, age, grade):
    with Session(engine) as session:
        session.execute(text(f"UPDATE students SET name = '{name}', age = '{age}', grade = '{grade}' WHERE id = {id}"))
        session.commit()


addStudents()

student2 = getStudentById(2)
print(f'{student2.name}, {student2.age}, {student2.grade}')

updateStudentById(2, 'Jacek Krzynówek', 42, 5.5)
student2 = getStudentById(2)
print(f'{student2.name}, {student2.age}, {student2.grade}')