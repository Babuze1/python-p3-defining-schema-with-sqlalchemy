# test_script.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_sandbox import Student  

engine = create_engine('sqlite:///students.db')

Session = sessionmaker(bind=engine)
session = Session()

new_student = Student(name="John Doe")
session.add(new_student)
session.commit()

session.close()
