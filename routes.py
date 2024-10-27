# Import necessary modules
from flask import Flask, jsonify, request  # Import Flask and request handling functions
from flask_restful import Resource, Api  # Import Flask-RESTful's Resource and Api classes
from models import db, Episode, Guest, Appearance  # Import the database and models

# Create a Flask application instance
app = Flask(__name__)

# Create an API instance
api = Api(app)

# Episode Resource
class EpisodeResource(Resource):
    # GET method to retrieve episodes or a specific episode by ID
    def get(self, id=None):
        if id is None:
            # If no ID is provided, return all episodes
            episodes = Episode.query.all()  # Query all episodes from the database
            return [{'id': e.id, 'date': e.date, 'number': e.number} for e in episodes]
        else:
            # If an ID is provided, return the specific episode
            episode = Episode.query.get(id)  # Query the episode by ID
            if episode:
                return {
                    'id': episode.id,  # Return the episode ID
                    'date': episode.date,  # Return the episode date
                    'number': episode.number,  # Return the episode number
                    'appearances': [{
                        'id': a.id,  # Appearance ID
                        'guest_id': a.guest_id,  # Guest ID associated with this appearance
                        'guest': {
                            'id': a.guest.id,  # Guest ID
                            'name': a.guest.name,  # Guest name
                            'occupation': a.guest.occupation  # Guest occupation
                        },
                        'rating': a.rating  # Appearance rating
                    } for a in episode.appearances]  # List of appearances for the episode
                }
            return {'error': 'Episode not found'}, 404  # Return an error if episode not found

# Guest Resource
class GuestResource(Resource):
    # GET method to retrieve a specific guest by ID
    def get(self, id):
        guest = Guest.query.get(id)  # Query the guest by ID
        if guest:
            return {
                'id': guest.id,  # Return the guest ID
                'name': guest.name,  # Return the guest name
                'occupation': guest.occupation  # Return the guest occupation
            }
        return {'error': 'Guest not found'}, 404  # Return an error if guest not found

# Appearance Resource
class AppearanceResource(Resource):
    # GET method to retrieve appearances or a specific appearance by ID
    def get(self, id=None):
        if id is None:
            # If no ID is provided, return all appearances
            appearances = Appearance.query.all()  # Query all appearances from the database
            return [{
                'id': a.id,  # Appearance ID
                'rating': a.rating,  # Appearance rating
                'episode_id': a.episode_id,  # Episode ID associated with this appearance
                'guest_id': a.guest_id,  # Guest ID associated with this appearance
                'episode': {
                    'id': a.episode.id,  # Episode ID
                    'date': a.episode.date,  # Episode date
                    'number': a.episode.number  # Episode number
                },
                'guest': {
                    'id': a.guest.id,  # Guest ID
                    'name': a.guest.name,  # Guest name
                    'occupation': a.guest.occupation  # Guest occupation
                }
            } for a in appearances]  # List of all appearances
        else:
            # If an ID is provided, return the specific appearance
            appearance = Appearance.query.get(id)  # Query the appearance by ID
            if appearance:
                return {
                    'id': appearance.id,  # Return the appearance ID
                    'rating': appearance.rating,  # Return the appearance rating
                    'episode_id': appearance.episode_id,  # Episode ID
                    'guest_id': appearance.guest_id  # Guest ID
                }
            return {'error': 'Appearance not found'}, 404  # Return an error if appearance not found

# Add Resources to API with their corresponding endpoints
api.add_resource(EpisodeResource, '/episodes', '/episodes/<int:id>')  # Endpoint for episodes
api.add_resource(GuestResource, '/guests/<int:id>')  # Endpoint for guests
api.add_resource(AppearanceResource, '/appearances', '/appearances/<int:id>')  # Endpoint for appearances

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask application in debug mode
