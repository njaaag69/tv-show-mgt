# TV Show Management Project

This project is a Flask-based web application designed to manage TV shows, episodes, guests, and their appearances. It provides RESTful API endpoints to interact with the data.

## Table of Contents

- [Technologies Used]
- [Project Setup]
- [Running the Application]
- [Seeding Data]
- [Database Migrations]
- [API Endpoints]


## Technologies Used

- **Python**: Programming language.
- **Flask**: Web framework for building the application.
- **Flask-SQLAlchemy**: ORM for database management.
- **Flask-Migrate**: Handling database migrations.
- **Flask-RESTful**: Extension for building REST APIs.
- **SQLite**: Database for storing data (can be replaced with other databases).
- **Postman**: Tool for testing API endpoints.

## Project Setup

Set up a virtual environment:


python -m venv venv
Activate the virtual environment:

Pipenv install && pipenv shell or;

On Windows:
venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate
Install required packages:

pip install -r requirements.txt

Configure the application: Update the config.py file with your database configurations if necessary.

Running the Application
Set environment variables (optional):


export FLASK_APP=app.py


Run the application:


python app.py
The application will be running on http://127.0.0.1:5555.

Seeding Data
To populate the database with initial data, follow these steps:

Run the seeding script:


python seed.py

Database Migrations
To manage database schema changes, use Flask-Migrate:

Initialize migrations:

flask db init
Create a migration script: Whenever you make changes to your models, run:

flask db migrate -m "Description of changes"
Apply the migration:

flask db upgrade
These commands will help keep your database schema in sync with your application models.

API Endpoints
Here are the available API endpoints:

Episodes:

GET /episodes: Retrieve all episodes.
GET /episodes/<int:id>: Retrieve a specific episode by ID.
Guests:

GET /guests: Retrieve all guests.
GET /guests/<int:id>: Retrieve a specific guest by ID.
Appearances:

GET /appearances: Retrieve all appearances.
POST /appearances: Create a new appearance.