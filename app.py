# Import necessary modules and classes from Flask and extensions
from flask import Flask  # Flask class to create the application
from models import db  # Import the database object from models
from routes import EpisodeResource, GuestResource, AppearanceResource  # Import resources for handling API requests
from config import Config  # Import configuration settings for the app
from flask_migrate import Migrate  # Import Migrate for handling database migrations
from flask_restful import Api  # Import Api for creating RESTful APIs

# Create an instance of the Flask application
app = Flask(__name__)  # The __name__ variable helps Flask know where to look for resources

# Load configuration settings from the Config class
app.config.from_object(Config)  # Configure the app with settings defined in Config

# Initialize the database with the Flask app
db.init_app(app)  # Bind the database to the app

# Create an instance of Migrate to manage database migrations
migrate = Migrate(app, db)  # Link the app and database for migrations

# Create an API instance for handling RESTful requests
api = Api(app)  # Instantiate the Api class to add resources for the application

# Add resources (endpoints) to the API
api.add_resource(EpisodeResource, '/episodes', '/episodes/<int:id>')  # Map EpisodeResource to /episodes and /episodes/<id>
api.add_resource(GuestResource, '/guests/<int:id>')  # Map GuestResource to /guests/<id>
api.add_resource(AppearanceResource, '/appearances', '/appearances/<int:id>')  # Map AppearanceResource to /appearances and /appearances/<id>

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True, port=5555)  # Start the Flask development server in debug mode on port 5555
