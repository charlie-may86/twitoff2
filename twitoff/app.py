from flask import Flask
# from .db_model import db, user

def create_app():
    '''Create and configure an instance of the Flask application'''

    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'Welcome to Twitoff!'

    return app
