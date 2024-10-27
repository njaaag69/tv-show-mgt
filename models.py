# Import the necessary modules
from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy for database interaction
from datetime import datetime  # Import datetime for handling date and time

# Initialize the SQLAlchemy database instance
db = SQLAlchemy()

# Define the Episode model
class Episode(db.Model):
    __tablename__ = 'episodes'  # Specify the name of the database table
    
    # Define columns for the Episode table
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the episode
    date = db.Column(db.String(10), nullable=False)  # Date of the episode (stored as a string)
    number = db.Column(db.Integer, nullable=False)  # Episode number
    
    # Define a relationship to the Appearance model
    appearances = db.relationship('Appearance', back_populates='episode', cascade="all, delete")
    # This allows access to all appearances related to an episode and specifies cascading deletes

# Define the Guest model
class Guest(db.Model):
    __tablename__ = 'guests'  # Specify the name of the database table
    
    # Define columns for the Guest table
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the guest
    name = db.Column(db.String(100), nullable=False)  # Name of the guest
    occupation = db.Column(db.String(100), nullable=False)  # Occupation of the guest
    
    # Define a relationship to the Appearance model
    appearances = db.relationship('Appearance', back_populates='guest', cascade="all, delete")
    # This allows access to all appearances related to a guest and specifies cascading deletes

# Define the Appearance model
class Appearance(db.Model):
    __tablename__ = 'appearances'  # Specify the name of the database table
    
    # Define columns for the Appearance table
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the appearance
    rating = db.Column(db.Integer, nullable=False)  # Rating for the appearance
    
    # Foreign keys to establish relationships with Episode and Guest
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)  # Reference to the associated episode
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)  # Reference to the associated guest
    
    # Define relationships back to Episode and Guest
    episode = db.relationship('Episode', back_populates='appearances')  # Relationship to Episode
    guest = db.relationship('Guest', back_populates='appearances')  # Relationship to Guest

    # Validation for rating
    @db.validates('rating')  # Decorator for validation on the rating field
    def validate_rating(self, key, value):
        # Ensure the rating is between 1 and 5
        if value < 1 or value > 5:
            raise ValueError("Rating must be between 1 and 5.")  # Raise an error if the rating is out of bounds
        return value  # Return the validated value
