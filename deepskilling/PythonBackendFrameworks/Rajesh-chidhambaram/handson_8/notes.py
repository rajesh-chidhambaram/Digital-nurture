# RESTful API Design Best Practices

"""
TASK 1 - Audit and Fix Resource Naming and HTTP Methods

STEP 78 - Resource Naming Audit
REST Naming Rules

1. Use nouns instead of verbs.
Good:
    /api/v1/courses/
Bad:
    /api/getCourses/
2. Use plural resource names.
Good:
    /courses/
    /students/
    /enrollments/
3. Use hyphens for multi-word resources.
Good:
    /course-categories/
Bad:
    /course_categories/

    
STEP 79 - HTTP Methods

Verified REST methods:
GET
- Read data
POST
- Create new resource
PUT
- Replace entire resource
PATCH
- Update only provided fields
DELETE
- Remove resource

Added:
PATCH /api/v1/courses/{course_id}

Difference:
PUT
- Full update
- All fields expected

PATCH
- Partial update
- Only supplied fields updated


STEP 80 - HTTP Status Codes

Implemented standard REST status codes.
200 OK
- GET
- PUT
- PATCH
201 Created
- POST
204 No Content
- DELETE
404 Not Found
- Resource does not exist
422 Unprocessable Entity
- Validation errors
- Automatically handled by FastAPI
401 Unauthorized
- Used when authentication is required.


STEP 81 - Location Header

Added Location header to POST responses.
Example:
Location:
/api/v1/courses/5


Implemented for:

Courses
Students
Enrollments
"""


"""
TASK 2 - Versioning, Pagination and Standardized Error Responses

STEP 82 - API Versioning

Changed routes from:
/api/courses/
to
/api/v1/courses/

Purpose:
- Supports future API versions.
- Allows backward compatibility.

Versioning Strategies
1. URL Versioning
Example:
/api/v1/courses/

2. Header Versioning
Example:
Accept:
application/vnd.api+json;version=1


STEP 83 - Offset Pagination

Added query parameters:
page
page_size
Pagination Formula:
offset = (page - 1) * page_size


STEP 84 - Search Filtering

Added:
search=
Searches:
Course Name
Course Code

Implemented using:
ilike()
or_()

STEP 85 - Standardized Error Responses

Created a global exception handler.
Previous Format
{
    "detail":"Course not found"
}

New Standard Format
{
    "error":{
        "code":"NOT_FOUND",
        "message":"Course with id 99 does not exist",
        "field":null
    }
}

Benefits
Consistent API responses
Easy frontend integration
Better debugging
Improved API documentation
"""


