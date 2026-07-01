from typing import Optional

from fastapi import (
    BackgroundTasks,
    Depends,
    FastAPI,
    HTTPException,
    Request,
    Response,
    status,
)
from fastapi.responses import JSONResponse

from sqlalchemy import func, or_, select
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

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": "NOT_FOUND"
                if exc.status_code == 404
                else "ERROR",

                "message": exc.detail,

                "field": None
            }
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
    "/api/v1/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Courses"],
    summary="Create a new course",
    response_description="The newly created course"
)
async def create_course(
    course: CourseCreate,
    response: Response,
    db: AsyncSession = Depends(get_db)
):
    new_course = Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id
    )
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)
    response.headers["Location"] = f"/api/v1/courses/{new_course.id}"
    return new_course

@app.get(
    "/api/v1/courses/",
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
    "/api/v1/courses/",
    tags=["Courses"],
    summary="Retrieve all courses"
)
async def get_courses(
    request: Request,
    page: int = 1,
    page_size: int = 10,
    department_id: Optional[int] = None,
    search: Optional[str] = None, 
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Course)

    if department_id is not None:
        stmt = stmt.where(
            Course.department_id == department_id
        )

    if search:
        stmt = stmt.where(
            or_(
                Course.name.ilike(f"%{search}%"),
                Course.code.ilike(f"%{search}%")
            )
        )

    total = await db.scalar(
        select(func.count()).select_from(stmt.subquery())
    )

    offset = (page - 1) * page_size
    stmt = stmt.offset(offset).limit(page_size)
    result = await db.execute(stmt)
    courses = result.scalars().all()
    next_url = None
    previous_url = None
    if offset + page_size < total:
        next_url = str(
            request.url.include_query_params(
                page=page + 1,
                page_size=page_size
            )
        )

    if page > 1:
        previous_url = str(
            request.url.include_query_params(
                page=page - 1,
                page_size=page_size
            )
        )

    return {
        "count": total,
        "next": next_url,
        "previous": previous_url,
        "results": courses
    }


@app.put(
    "/api/v1/courses/{course_id}",
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


@app.patch(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse,
    tags=["Courses"],
    summary="Partially update a course"
)
async def patch_course(
    course_id: int,
    course: CourseUpdate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    db_course = result.scalar_one_or_none()

    if db_course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )

    updates = course.model_dump(exclude_unset=True)

    for field, value in updates.items():
        setattr(db_course, field, value)

    await db.commit()
    await db.refresh(db_course)

    return db_course


@app.delete(
    "/api/v1/courses/{course_id}",
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
    "/api/v1/students/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Students"],
    summary="Create a new student"
)
async def create_student(
    student: StudentCreate,
    response: Response,
    db: AsyncSession = Depends(get_db)
):

    new_student = Student(
        name=student.name,
        email=student.email
    )
    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)
    response.headers["Location"] = f"/api/v1/students/{new_student.id}"
    return new_student


@app.get(
    "/api/v1/students/",
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
    "/api/v1/enrollments/",
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
    response.headers["Location"] = f"/api/v1/enrollments/{new_enrollment.id}"
    return new_enrollment

@app.get(
    "/api/v1/enrollments/",
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
        "/api/v1/courses/{course_id}/students/", 
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