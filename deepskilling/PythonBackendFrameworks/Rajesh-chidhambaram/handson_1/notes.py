# Web Framework Foundations & Django Project Setup

# Task 1 -  Understand the Request-Response Cycle
"""
STEP 1 - Django Request Response Cycle
Example Request: GET /api/courses/

1. Browser sends HTTP request to Django server.
2. Django URL Router (urls.py) receives the request and finds the matching URL pattern.
3. The matched View function/class is executed.
4. The View interacts with the Model layer. Example:Course.objects.all()
5. Model performs SQL query on the database.
6. Database returns results to the Model.
7. Model returns data to the View.
8. View prepares an HTTP Response.
9. Response is sent back through Django.
10. Browser receives and displays the response.

Browser --> URL --> Router --> View --> Model --> Database --> View --> Response --> Browser


STEP 2 - Middleware
Middleware sits between the incoming request and the Django View.
Request Flow:
Browser --> Middleware --> URL Router --> View --> Response --> Middleware --> Browser

Built-in Middleware Examples:
1. SecurityMiddleware - Adds security-related headers and protections.
2. SessionMiddleware - Manages user session data across requests.


STEP 3 - WSGI vs ASGI
WSGI (Web Server Gateway Interface)
- Traditional Python web server interface.
- Handles synchronous requests.
- One request processed at a time per worker.

Examples:
Django (default)
Flask
Gunicorn

ASGI (Asynchronous Server Gateway Interface)
- Modern asynchronous interface.
- Supports async/await.
- Handles WebSockets and long-lived connections.
- Better for high concurrency applications.

Django uses WSGI by default.

Switch to ASGI when:
- Using WebSockets
- Building chat applications
- Real-time notifications
- High-concurrency APIs
- Async database operations


STEP 4 - MVC vs Django MVT
MVC Pattern:
Model      -> Data and database logic
View       -> User interface
Controller -> Handles request logic

Django follows MVT:

Model
   -> Same as MVC Model

View
   -> Acts like MVC Controller
   -> Handles business logic and requests

Template
   -> Acts like MVC View
   -> Responsible for displaying data

Mapping:
MVC Model       -> Django Model
MVC View        -> Django Template
MVC Controller  -> Django View
"""

# Task 2 - Scaffold and Explore the Django Project
"""
STEP 5 - Create the Django Project

Commands Used: 'django-admin startproject coursemanager'

Purpose of Files:

manage.py
- Command-line utility for managing the project.

settings.py
- Main configuration file.
- Contains installed apps, database settings, middleware, templates, etc.

urls.py
- Defines URL routing for the project.

wsgi.py
- Entry point for WSGI servers.
- Used for synchronous deployments.

asgi.py
- Entry point for ASGI servers.
- Supports async applications and WebSockets.


STEP 6 - Create the Courses App

Command Used: 'python manage.py startapp courses'

Purpose:
- Apps are reusable modules inside a Django project.
- The courses app contains course-related functionality.


STEP 7 - Register the App

Added 'courses' inside INSTALLED_APPS in settings.py.

Purpose:
- Tells Django to include the app in the project.
- Enables models, migrations and admin integration.


STEP 8 - Create a Basic View

Created hello_view() in views.py.

Purpose:
- Handles incoming HTTP requests.
- Returns a simple HTTP response.

Example:
GET /api/hello/

Response:
Course Management API is running


STEP 9 - Configure URLs

Created:
courses/urls.py

Used include() in project urls.py.

Purpose:
- Keeps URL configuration modular and maintainable.


STEP 10 - Run Development Server

Command: 'python manage.py runserver'

Default URL:
http://127.0.0.1:8000/

Test Endpoint:
http://127.0.0.1:8000/api/hello/

Expected Output:
Course Management API is running

"""
