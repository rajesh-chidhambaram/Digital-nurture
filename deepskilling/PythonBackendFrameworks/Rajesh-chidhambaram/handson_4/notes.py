# Flask - App Structure, Routing, Jinja2 & Blueprints

"""
TASK 1 - Flask App Structure and Basic Routing

STEP 36 - Create Flask Project

Installed Packages:
- Flask
- Flask-SQLAlchemy
- Flask-Migrate

Purpose:
- Set up a Flask project with a modular structure.
- Prepare for database integration in future hands-ons.


STEP 37 - Create Flask Application

Created:
- create_app() function
- Flask application instance

Purpose:
- Uses the Application Factory Pattern.
- Loads configuration.
- Registers Blueprints.
- Returns the Flask application.


STEP 38 - Configuration

Created:
config.py

Added:
- SECRET_KEY
- SQLALCHEMY_DATABASE_URI
- SQLALCHEMY_TRACK_MODIFICATIONS
- DEBUG

Purpose:
- Centralizes application configuration.
- Keeps configuration separate from application logic.


STEP 39 - Create Blueprint

Created:

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)

Purpose:
- Organizes related routes.
- Improves project modularity.
- Similar to Django Apps.


STEP 40 - Register Blueprint

Registered:

app.register_blueprint(courses_bp)

Purpose:
- Makes Blueprint routes available to the application.
- Without registration, Flask cannot access Blueprint routes.


STEP 41 - Run Flask Application

Command:

python app.py

Test Endpoint:

GET
/api/courses/

Outcome:
- Flask server running successfully.
- Blueprint routes accessible.
"""


"""
TASK 2 - Flask CRUD APIs

STEP 42 - In-Memory Data Storage

Created:

courses = [
    {...},
    {...}
]

Purpose:
- Store course data temporarily in memory.
- Used before introducing databases.

Limitation:
- Data is lost when the server restarts.


STEP 43 - CRUD Operations

Implemented Endpoints:

GET
/api/courses/

- Retrieve all courses.


GET
/api/courses/<id>

- Retrieve a specific course.


POST
/api/courses/

- Create a new course.


PUT
/api/courses/<id>

- Update an existing course.


DELETE
/api/courses/<id>

- Delete a course.


STEP 44 - Request Validation

Used:

request.get_json()

Validated Required Fields:
- name
- code
- credits

Purpose:
- Prevent invalid requests.
- Return appropriate error messages.
- Improve API reliability.


STEP 45 - Global Error Handler

Implemented:

@app.errorhandler(404)

Purpose:
- Return JSON response for unknown routes.
- Replace default HTML error page.

Example:

GET /random

Response:

{
    "error": "Resource not found"
}

Note:
- Handles only undefined routes.
- Does not handle errors returned manually inside route functions.


STEP 46 - API Testing

Tested Using:
- Postman

Verified:
- GET
- POST
- PUT
- DELETE

Outcome:
- CRUD APIs working successfully.
- Input validation implemented.
- Global error handling configured.
"""

