"""
TASK 3 - N+1 QUERY ANALYSIS

Without joinedload():
1 query for enrollments
N queries for students
N queries for courses

With joinedload():
Single JOIN query fetches everything.

Django Equivalent:
Enrollment.objects.select_related(
    'student',
    'course'
).all()
"""


from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import joinedload, sessionmaker

from models import (
    Department,
    Student,
    Course,
    Enrollment
)

engine = create_engine(
    "mysql+mysqlconnector://root:your_password@localhost/college_db_orm",
    echo=True
)

Session = sessionmaker(bind=engine)
session = Session()


# TASK 2

# Step 81: INSERT Departments

cs_department = Department(
    dept_name="Computer Science",
    head_of_dept="Dr. Kumar",
    budget=500000
)

it_department = Department(
    dept_name="Information Technology",
    head_of_dept="Dr. Sharma",
    budget=450000
)

ece_department = Department(
    dept_name="Electronics",
    head_of_dept="Dr. Rao",
    budget=400000
)

session.add_all([
    cs_department,
    it_department,
    ece_department
])

session.commit()

print("Departments inserted successfully")


# INSERT Students

student1 = Student(
    first_name="Raj",
    last_name="Kumar",
    email="raj@gmail.com",
    date_of_birth=date(2002, 5, 10),
    department_id=cs_department.department_id,
    enrollment_year=2022
)

student2 = Student(
    first_name="Arjun",
    last_name="Singh",
    email="arjun@gmail.com",
    date_of_birth=date(2002, 7, 12),
    department_id=cs_department.department_id,
    enrollment_year=2022
)

student3 = Student(
    first_name="Priya",
    last_name="Nair",
    email="priya@gmail.com",
    date_of_birth=date(2001, 9, 5),
    department_id=it_department.department_id,
    enrollment_year=2021
)

student4 = Student(
    first_name="Meera",
    last_name="Reddy",
    email="meera@gmail.com",
    date_of_birth=date(2002, 1, 15),
    department_id=ece_department.department_id,
    enrollment_year=2023
)

student5 = Student(
    first_name="Kiran",
    last_name="Das",
    email="kiran@gmail.com",
    date_of_birth=date(2001, 12, 20),
    department_id=it_department.department_id,
    enrollment_year=2021
)

session.add_all([
    student1,
    student2,
    student3,
    student4,
    student5
])

session.commit()

print("Students inserted successfully")


# Step 82: INSERT Courses

course1 = Course(
    course_name="Database Systems",
    course_code="CS101",
    credits=4,
    department_id=cs_department.department_id
)

course2 = Course(
    course_name="Web Development",
    course_code="CS102",
    credits=3,
    department_id=cs_department.department_id
)

course3 = Course(
    course_name="Computer Networks",
    course_code="CS103",
    credits=4,
    department_id=it_department.department_id
)

session.add_all([
    course1,
    course2,
    course3
])

session.commit()

print("Courses inserted successfully")


# INSERT Enrollments

enrollment1 = Enrollment(
    student_id=student1.student_id,
    course_id=course1.course_id,
    enrollment_date=date.today(),
    grade="A"
)

enrollment2 = Enrollment(
    student_id=student1.student_id,
    course_id=course2.course_id,
    enrollment_date=date.today(),
    grade="B"
)

enrollment3 = Enrollment(
    student_id=student2.student_id,
    course_id=course1.course_id,
    enrollment_date=date.today(),
    grade="A"
)

enrollment4 = Enrollment(
    student_id=student3.student_id,
    course_id=course3.course_id,
    enrollment_date=date.today(),
    grade="B"
)

session.add_all([
    enrollment1,
    enrollment2,
    enrollment3,
    enrollment4
])

session.commit()

print("Enrollments inserted successfully")


# Step 83: READ Students from Computer Science Department

print("\nStudents in Computer Science Department:\n")

students = (
    session.query(Student)
    .join(Department)
    .filter(
        Department.dept_name == "Computer Science"
    )
    .all()
)

for student in students:
    print(
        student.student_id,
        student.first_name,
        student.last_name
    )


# Step 84: READ Enrollment Details

print("\nEnrollment Details:\n")

enrollments = session.query(Enrollment).all()

for enrollment in enrollments:
    print(
        enrollment.student.first_name,
        "->",
        enrollment.course.course_name
    )


# Step 85: UPDATE Student

student = (
    session.query(Student)
    .filter(
        Student.email == "raj@gmail.com"
    )
    .first()
)

if student:
    student.enrollment_year = 2024
    session.commit()

    print(
        f"\nUpdated enrollment year for {student.first_name}"
    )


# Step 86: DELETE Enrollment

enrollment = (
    session.query(Enrollment)
    .filter(
        Enrollment.student_id == student3.student_id
    )
    .first()
)

if enrollment:
    session.delete(enrollment)
    session.commit()

    print("\nEnrollment deleted successfully")


# Verification

remaining = session.query(Enrollment).all()

print("\nRemaining Enrollments:")

for enrollment in remaining:
    print(
        enrollment.enrollment_id,
        enrollment.student_id,
        enrollment.course_id
    )

# Step 87 : Identify N+1 Problem

print("\nStep 87: Check SQL logs above.")
print("Multiple SELECT statements indicate the N+1 problem.")


# Step 88 & 89 : Optimized Query using joinedload()

print("\nEnrollment Details using joinedload():\n")

optimized_enrollments = (
    session.query(Enrollment)
    .options(
        joinedload(Enrollment.student),
        joinedload(Enrollment.course)
    )
    .all()
)

for enrollment in optimized_enrollments:
    print(
        enrollment.student.first_name,
        "->",
        enrollment.course.course_name
    )

print("\njoinedload() fetches related data using a single JOIN query.")


# Step 90 : Comparison documented at the top of this file.


# Step 91 :Django ORM Equivalent

print("\nDjango ORM Equivalent:")

print("""
Enrollment.objects.select_related(
    'student',
    'course'
).all()
""")

session.close()