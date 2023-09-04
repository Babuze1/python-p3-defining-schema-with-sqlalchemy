from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_sandbox import Student  

engine = create_engine('sqlite:///students.db')

Session = sessionmaker(bind=engine)
session = Session()

new_student = Student(name="John Doe")
session.add(new_student)
session.commit()

students = session.query(Student).all()
for student in students:
    print(f"ID: {student.id}, Name: {student.name}")

session.close()