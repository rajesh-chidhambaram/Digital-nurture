# Django REST Framework (DRF)

"""
TASK 1 - Serializers and Basic API Views

STEP 26 - Create Serializers

Created:
- DepartmentSerializer
- CourseSerializer
- StudentSerializer
- EnrollmentSerializer

Purpose:
- Converts Django model instances into JSON.
- Converts JSON request data into Django model objects.


STEP 27 - Create CourseListView

Used:
APIView

Implemented:

GET /api/courses/
POST /api/courses/

Purpose:
- Retrieve all courses.
- Create a new course.

Methods:
get()
post()


STEP 28 - Create CourseDetailView

Implemented:

GET    /api/courses/<id>/
PUT    /api/courses/<id>/
DELETE /api/courses/<id>/

Purpose:
- Retrieve a specific course.
- Update a course.
- Delete a course.

Methods:
get()
put()
delete()


STEP 29 - Configure URLs

Added routes:

path(
    "courses/",
    CourseListView.as_view()
)

path(
    "courses/<int:pk>/",
    CourseDetailView.as_view()
)

Purpose:
- Connect API endpoints to views.


STEP 30 - Test APIs

Tested:
GET
POST
PUT
DELETE

using:
- Browser
- Postman

"""


"""
TASK 2 - ViewSets and Routers

STEP 31 - Reuse Existing Serializers

Used:
- CourseSerializer
- StudentSerializer

Purpose:
- Serialize Course and Student data for API responses.


STEP 32 - Create CourseViewSet

Used:
class CourseViewSet(viewsets.ModelViewSet)

Purpose:
- Automatically provides CRUD operations.

Generated Endpoints:
GET
POST
PUT
DELETE

without manually writing methods.


STEP 33 - Configure Router

Used:
from rest_framework.routers import DefaultRouter

router.register(
    "courses",
    CourseViewSet
)

Purpose:
- Automatically generates URL patterns.
- Reduces manual routing code.

Generated Routes:
/api/courses/
/api/courses/<id>/


STEP 34 - Add Custom Action

Added:
@action(
    detail=True,
    methods=["get"]
)

Endpoint:
/api/courses/<id>/students/

Purpose:
- Retrieve students enrolled in a specific course.

STEP 35 - Test ViewSet APIs

Tested:
GET /api/courses/

GET /api/courses/1/

POST /api/courses/

DELETE /api/courses/1/

GET /api/courses/2/students/

"""


"""
KEY DRF CONCEPTS LEARNED

1. Serializer
   - Converts Model <--> JSON

2. APIView
   - Class-based API development.
   - Full control over request handling.

3. Response
   - DRF response object.
   - Automatically returns JSON.

4. Status Codes
   200 OK
   201 Created
   204 No Content
   400 Bad Request
   404 Not Found

5. ModelViewSet
   - Provides complete CRUD functionality.
   - Reduces boilerplate code.

6. Router
   - Automatically generates URLs.

7. Custom Action
   - Creates custom endpoints inside ViewSets.

8. REST API Endpoints

   GET     -> Read
   POST    -> Create
   PUT     -> Update
   PATCH   -> Partial Update
   DELETE  -> Delete

9. API Flow

   Client
      ↓
   URL
      ↓
   View / ViewSet
      ↓
   Serializer
      ↓
   Model
      ↓
   Database
      ↓
   JSON Response

"""