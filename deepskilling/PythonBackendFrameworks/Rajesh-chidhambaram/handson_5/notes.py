# Flask with SQLAlchemy ORM & Database Integration

"""
TASK 1 - Define SQLAlchemy Models and Migrations

STEP 47 - Initialize SQLAlchemy

Created:
- SQLAlchemy()
- Migrate()

Purpose:
- Connect Flask with a database.
- Manage database migrations.

Methods Used:
- db.init_app(app)
- migrate.init_app(app, db)


STEP 48 - Create Course Model

Created:

class Course(db.Model)

Added Fields:
- id
- name
- code
- credits

Purpose:
- Represents the Course table.
- Maps Python objects to database records.

Methods:
- to_dict()

STEP 49 - Register Models

Imported model inside package initialization.

Purpose:
- Allows Flask-Migrate to detect models.
- Required before generating migrations.


STEP 50 - Database Migration

Commands:

flask --app app db init

flask --app app db migrate -m "Initial migration"

flask --app app db upgrade

Purpose:
- Initialize migration repository.
- Generate migration scripts.
- Create database tables.


STEP 51 - Verify Database

Verified:
- Database created successfully.
- Courses table generated.
- Alembic version table generated.

"""


"""
TASK 2 - Connect ORM to API Routes

STEP 52 - Replace In-Memory Storage

Removed:
- Python list storage.

Replaced With:
- SQLite database.
- SQLAlchemy ORM queries.


STEP 53 - Implement CRUD Operations

GET All - Course.query.all()

Purpose:
- Retrieve all course records.


GET By ID - Course.query.get(id)

Purpose:
- Retrieve a specific course.


POST 
db.session.add(course)
db.session.commit()

Purpose:
- Insert a new course.


PUT - Update model attributes.

db.session.commit()

Purpose:
- Save updated course details.


DELETE
db.session.delete(course)

db.session.commit()

Purpose:
- Remove a course from the database.


STEP 54 - Test CRUD APIs

Verified:
- GET
- POST
- PUT
- DELETE


STEP 55 - Data Persistence

Verified:
- Data remains after restarting Flask server.

Difference:

In-Memory Storage
- Temporary
- Lost after restart

SQLite Database
- Persistent
- Stored permanently


STEP 56 - Verify Database Contents

Verified:
- Records stored successfully.
- Table creation successful.
- CRUD operations reflected in database.
"""
