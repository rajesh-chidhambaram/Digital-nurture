# FastAPI Framework - Pydantic Validation, Async SQLAlchemy & CRUD APIs

"""
TASK 1 - FastAPI Setup and Pydantic Schemas

STEP 57 - Create FastAPI Application

Created:

app = FastAPI(
    title="Course Management API",
    version="1.0"
)

Purpose:
- Initializes the FastAPI application.
- Adds API metadata for documentation.

Added Root Endpoint:

GET /

Response:

{
    "message": "API running"
}

Run Application:

uvicorn main:app --reload

Default URL:

http://127.0.0.1:8000


STEP 58 - Create Pydantic Schemas

Created:

CourseCreate
CourseUpdate
CourseResponse
DepartmentResponse

Purpose:
- Validate request data.
- Define API response structure.
- Improve type safety.


STEP 59 - Nested Models

Created:

DepartmentResponse

Containing:

courses: list[CourseResponse]

Purpose:
- Demonstrates nested JSON responses.
- Represents one-to-many relationships.


STEP 60 - Create POST Endpoint

Endpoint:

POST
/api/courses/

Input:

CourseCreate

Purpose:
- Accept JSON request body.
- Automatically validate using Pydantic.

No manual validation required.


STEP 61 - Swagger Documentation

Documentation URLs:

http://127.0.0.1:8000/docs

http://127.0.0.1:8000/redoc

Features:
- Interactive API testing.
- Request/Response schemas.
- Auto-generated OpenAPI documentation.

"""


"""
TASK 2 - Path/Query Parameters and Async Database Access

STEP 62 - Path Parameters

Endpoint:

GET
/api/courses/{course_id}

Purpose:
- Retrieve a course using its ID.

Feature:
- FastAPI automatically validates path parameters.

Example:
GET /api/courses/1

Invalid:
GET /api/courses/abc

Returns:
422 Unprocessable Entity


STEP 63 - Query Parameters

Endpoint:

GET
/api/courses/

Query Parameters:
skip
limit
department_id

Purpose:
- Pagination
- Filtering

Examples:

GET /api/courses/?skip=0&limit=5

GET /api/courses/?department_id=1


STEP 64 - Async SQLAlchemy Configuration

Created:

database.py

Configured:

create_async_engine()

AsyncSession

sessionmaker()

get_db()

Purpose:
- Enable asynchronous database operations.
- Connect FastAPI with SQLite.

Database URL:

sqlite+aiosqlite:///./coursemanager.db


STEP 65 - Dependency Injection

Used:

Depends(get_db)

Purpose:
- Automatically provides a database session.
- Opens session before request.
- Closes session after request.

Example:

db: AsyncSession = Depends(get_db)


STEP 66 - Async CRUD Operations

Implemented:

Create

db.add()

await db.commit()

await db.refresh()

Read

await db.execute(select(Course))

Update

Modify object

await db.commit()

Delete

await db.delete()

await db.commit()

Purpose:
- Perform database operations asynchronously.


STEP 67 - Pagination and Filtering

Pagination:

offset(skip)

limit(limit)

Filtering:

where(Course.department_id == department_id)

Examples:

GET /api/courses/?skip=0&limit=2

GET /api/courses/?skip=2&limit=2

GET /api/courses/?department_id=1

"""
