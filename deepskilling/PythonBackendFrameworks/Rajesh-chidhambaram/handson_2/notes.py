# Django Models, Migrations and Admin Interface

"""
TASK 1 - Models and Database Migrations

STEP 11 - Create Models

Created Models:
1. Department
2. Course
3. Student
4. Enrollment

Relationships:
Department -> Courses (One-to-Many)
Department -> Students (One-to-Many)
Student -> Course (Many-to-Many through Enrollment)

STEP 12 - Add __str__ Methods

- Provides readable object names.
- Improves Admin Panel and Shell output.

Example:
Instead of: Course object (1)

Displays: Python Programming


STEP 13 - Generate Migrations

Command:
python manage.py makemigrations

- Converts model definitions into migration files.
- Django tracks schema changes through migrations.


STEP 14 - Apply Migrations

Command:
python manage.py migrate

- Creates database tables from migration files.
- Updates database schema.


STEP 15 - Prevent Duplicate Enrollments

Added:

class Meta:
    unique_together = [['student', 'course']]

- Prevents a student from enrolling in the same course multiple times.

Outcome:
- Database integrity maintained.
"""


"""
TASK 2 - Django ORM Queries

STEP 16 - Create Sample Data

Created:
- Departments
- Courses
- Students

- Populate database for testing ORM queries.


STEP 17 - Filter Data

Example:

Course.objects.filter(
    department__name="Computer Science"
)

- Retrieve records matching specific conditions.
- Demonstrates relationship traversal using '__'.


STEP 18 - Aggregation using annotate()

Used:

from django.db.models import Count

Department.objects.annotate(
    course_count=Count("course")
)

- Count courses per department.
- Generate summary statistics.


STEP 19 - Optimize Queries using select_related()

Used:

Student.objects.select_related("department")

- Prevents N+1 query problem.
- Retrieves related objects using SQL JOIN.
- Improves performance.


STEP 20 - Update Records using F Expressions

Used:

from django.db.models import F

Department.objects.update(
    budget=F("budget") * 1.10
)

- Perform database-side calculations.
- Avoid unnecessary object retrieval.
"""


"""
TASK 3 - Django Admin Interface

STEP 21 - Create Superuser

Command:
python manage.py createsuperuser

- Provides administrative access to Django Admin.


STEP 22 - Register Models

Registered:
- Department
- Course
- Student
- Enrollment

- Makes models visible inside Django Admin.


STEP 23 - Customize Course Admin

Added:
- list_display
- search_fields

- Improves data visibility.
- Enables search functionality.


STEP 24 - Add Filters

Added:

list_filter = ["department"]

- Quickly filter courses by department.


STEP 25 - Test Admin Functionality

Performed:
- Added records through Admin Panel.
- Created enrollments.
- Verified duplicate enrollment prevention.

"""