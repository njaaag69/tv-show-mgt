# Import necessary modules and classes from the application and models
from app import app  # Import the Flask application instance
from models import db, Episode, Guest, Appearance  # Import the database and models

# Use the application context to access the database
with app.app_context():
    db.create_all()  # Create all database tables based on the defined models

    # Seed Episodes
    episode1 = Episode(date="1/11/99", number=1)  # Create an instance of Episode
    episode2 = Episode(date="1/12/99", number=2)  # Create another instance of Episode
    db.session.add_all([episode1, episode2])  # Add episodes to the session

    # Seed Guests
    guest1 = Guest(name="Michael J. Fox", occupation="actor")  # Create a Guest instance
    guest2 = Guest(name="Sandra Bernhard", occupation="Comedian")  # Create another Guest
    guest3 = Guest(name="Tracey Ullman", occupation="television actress")  # Create another Guest
    db.session.add_all([guest1, guest2, guest3])  # Add guests to the session

    # Seed Appearances
    appearance1 = Appearance(rating=4, episode=episode1, guest=guest1)  # Create an Appearance instance linking an episode and a guest
    appearance2 = Appearance(rating=5, episode=episode2, guest=guest2)  # Create another Appearance instance
    db.session.add_all([appearance1, appearance2])  # Add appearances to the session

    db.session.commit()  # Commit the session to save all changes to the database
    print("My nigga! Database seeded successfully!")  # Print success message
