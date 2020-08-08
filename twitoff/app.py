from flask import Flask, render_template
from .db_model import db, User

def create_app():
    '''Create and configure an instance of the Flask application'''

    # /Users/charliemay/Desktop/Lambda/Unit3-Sprint-3-twitoff/twitoff2

    app_URI = "sqlite:////Users/charliemay/Desktop/Lambda/Unit3-Sprint-3-twitoff/twitoff2/twitoff2.sqlite"

    # connects to the DB
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = app_URI 
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html', title='Home', users=User.query.all())

    @app.route('/next')
    def next():
        return "You're doing it!"

    return app
