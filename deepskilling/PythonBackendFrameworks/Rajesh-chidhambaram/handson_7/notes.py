# FastAPI Advanced Features - RESTful CRUD, Background Tasks & OpenAPI Documentation

"""
TASK 1 - Complete CRUD with Proper HTTP Conventions

STEP 68 - Complete CRUD Operations

Implemented:

POST    /api/courses/
GET     /api/courses/
GET     /api/courses/{id}
PUT     /api/courses/{id}
DELETE  /api/courses/{id}

Purpose:
- Follow RESTful API conventions.
- Support complete Create, Read, Update and Delete operations.


STEP 68.1 - Response Models

Used:

response_model=CourseResponse

Purpose:
- Defines the structure of the API response.
- Automatically validates returned data.
- Hides unwanted fields from ORM objects.
- Improves Swagger documentation.

Examples:

response_model=CourseResponse

response_model=list[CourseResponse]


STEP 69 - Proper HTTP Status Codes

Used:

POST

status.HTTP_201_CREATED

Meaning:
- Resource created successfully.

DELETE
status.HTTP_204_NO_CONTENT

Meaning:
- Resource deleted successfully.
- No response body is returned.

Common Status Codes:
200 OK
201 Created
204 No Content
404 Not Found


STEP 70 - Error Handling

Used:
HTTPException

Example:
raise HTTPException(
    status_code=404,
    detail="Course not found"
)

Purpose:
- Returns proper JSON error responses.
- Stops endpoint execution immediately.

Response Example:

{
    "detail": "Course not found"
}


STEP 71 - JOIN Query

Created endpoint:
GET
/api/courses/{course_id}/students/

Purpose:
- Retrieve all students enrolled in a course.

SQLAlchemy Join:

select(Student)
.join(Enrollment)
.where(Enrollment.course_id == course_id)


STEP 72 - Student and Enrollment CRUD

Created Models:
Student
Enrollment 

Implemented CRUD Endpoints:

Students -
POST /api/students/
GET /api/students/

Enrollments -
POST /api/enrollments/
GET /api/enrollments/

Purpose:
- Manage students.
- Manage course enrollments.
- Demonstrate many-to-many relationships.
"""


"""
TASK 2 - Background Tasks and OpenAPI Customisation

STEP 73 - Background Tasks

Imported:
BackgroundTasks

Created:
send_confirmation_email(student_email)

Example:
def send_confirmation_email(student_email):
    print(f"Sending confirmation to {student_email}")

Purpose:
- Execute non-critical work after sending the response.
- Improve API responsiveness.


STEP 74 - Verify Background Task

Example:

Sending confirmation to rajesh@example.com

Benefit:
- User does not wait for email processing.


STEP 75 - OpenAPI Metadata

Customized FastAPI application:

app = FastAPI(
    title=...,
    description=...,
    version=...,
    contact={...}
)

Displayed in:

http://127.0.0.1:8000/docs

Purpose:
- Improves API documentation.
- Provides project information.


STEP 76 - Tags

Used:

tags=["Courses"]
tags=["Students"]
tags=["Enrollments"]

Purpose:
- Organizes endpoints into groups.
- Makes Swagger UI easier to navigate.

Example:

Courses-
GET

POST -
PUT
DELETE

Students -
GET
POST

Enrollments - 
GET
POST


STEP 77 - Summary and Response Description

Added:
summary
response_description

Example:
summary="Create a new course"
response_description="The newly created course"

"""

