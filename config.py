# Import the os module to access environment variables and handle file paths
import os

# Define a configuration class for the application
class Config:
    # Set the URI for the SQLAlchemy database to use SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'  # This specifies that the database is an SQLite file named 'database.db'
    
    # Disable modification tracking for SQLAlchemy to reduce overhead
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # This setting is to avoid overhead associated with tracking modifications of objects, which is not necessary in most cases
