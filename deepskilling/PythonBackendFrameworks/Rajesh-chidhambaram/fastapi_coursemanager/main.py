from typing import Optional

from fastapi import (
    Depends,
    FastAPI,
    HTTPException,
    Response,
    status,
    BackgroundTasks,
)
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import Base, engine, get_db
from models import Course, Enrollment, Student
from schemas import (
    CourseCreate,
    CourseResponse,
    CourseUpdate,
    EnrollmentCreate,
    EnrollmentResponse,
    StudentCreate,
    StudentResponse,
)

def send_confirmation_email(student_email: str):
    print(f"Sending confirmation to {student_email}")

app = FastAPI(
    title="Course Management API",
    description="A RESTful API for managing courses, students, and enrollments using FastAPI and SQLAlchemy.",
    version="1.0.0",
    contact={
        "name": "Rajesh",
        "email": "rajesh@example.com",
    }
)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def root():
    return {
        "message": "API running"
    }


@app.post(
    "/api/courses/",
    tags=["Courses"],
    response_model=CourseResponse,
    summary="Create a new course",
    status_code=status.HTTP_201_CREATED,
)
async def create_course(
    course: CourseCreate,
    db: AsyncSession = Depends(get_db),
):
    new_course = Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id,
    )

    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)

    return new_course


@app.get(
    "/api/courses/",
    tags=["Courses"],
    response_model=list[CourseResponse],
    summary="Retrieve a list of courses",
)
async def get_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: Optional[int] = None,
    db: AsyncSession = Depends(get_db),
):
    stmt = select(Course)

    if department_id is not None:
        stmt = stmt.where(Course.department_id == department_id)

    stmt = stmt.offset(skip).limit(limit)

    result = await db.execute(stmt)
    courses = result.scalars().all()

    return courses


@app.get(
    "/api/courses/{course_id}",
    tags=["Courses"],
    response_model=CourseResponse,
    summary="Retrieve a specific course by ID"
)
async def get_course(
    course_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found",
        )

    return course


@app.put(
    "/api/courses/{course_id}",
    response_model=CourseResponse,
    tags=["Courses"],
    summary="Update a specific course by ID"
)
async def update_course(
    course_id: int,
    course: CourseUpdate,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    db_course = result.scalar_one_or_none()

    if db_course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found",
        )

    if course.name is not None:
        db_course.name = course.name

    if course.code is not None:
        db_course.code = course.code

    if course.credits is not None:
        db_course.credits = course.credits

    if course.department_id is not None:
        db_course.department_id = course.department_id

    await db.commit()
    await db.refresh(db_course)

    return db_course


@app.delete(
    "/api/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Courses"],
    summary="Delete a specific course by ID"
)
async def delete_course(
    course_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found",
        )

    await db.delete(course)
    await db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.post(
    "/api/students/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Students"],
    summary="Create a new student"
)
async def create_student(
    student: StudentCreate,
    db: AsyncSession = Depends(get_db)
):

    new_student = Student(
        name=student.name,
        email=student.email
    )

    db.add(new_student)

    await db.commit()

    await db.refresh(new_student)

    return new_student


@app.get(
    "/api/students/",
    tags=["Students"],
    response_model=list[StudentResponse],
    summary="Retrieve a list of students"
)
async def get_students(
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Student)
    )

    return result.scalars().all()


@app.post(
    "/api/enrollments/",
    tags=["Enrollments"],
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Enrollments"],
    summary="Enroll a student in a course"
)
async def create_enrollment(
    enrollment: EnrollmentCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    new_enrollment = Enrollment(
        course_id=enrollment.course_id,
        student_id=enrollment.student_id
    )

    db.add(new_enrollment)
    await db.commit()
    await db.refresh(new_enrollment)

    student_result = await db.execute(
        select(Student).where(Student.id == enrollment.student_id)
    )

    student = student_result.scalar_one()

    background_tasks.add_task(
        send_confirmation_email,
        student.email
    )

    return new_enrollment

@app.get(
    "/api/enrollments/",
    tags=["Enrollments"],
    response_model=list[EnrollmentResponse],
    summary="Retrieve a list of enrollments"
)
async def get_enrollments(
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Enrollment)
    )

    return result.scalars().all()


@app.get(
        "/api/courses/{course_id}/students/", 
        tags=["Courses"], 
        summary="Retrieve students enrolled in a specific course"
        )
async def get_course_students(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Student)
        .join(Enrollment)
        .where(Enrollment.course_id == course_id)
    )

    students = result.scalars().all()

    return students