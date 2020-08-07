'''Entry point to the Twitoff Flask application'''

from .app import create_app

# Global variable
APP = create_app()