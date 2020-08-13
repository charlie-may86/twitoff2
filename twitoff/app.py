from flask import Flask, render_template, request
from .db_model import db, User
from .twitter import add_user_twitter_scraper, update_all_users
from .predict import predict_user
import numpy as np
from .db_model import db, User
from dotenv import load_dotenv
from os import getenv

load_dotenv()

def create_app():
    '''Create and configure an instance of the Flask application'''

    # /Users/charliemay/Desktop/Lambda/Unit3-Sprint-3-twitoff/twitoff2

    app_URI = "sqlite:////Users/charliemay/Desktop/Lambda/Unit3-Sprint-3-twitoff/twitoff2/twitoff2.sqlite"

    # connects to the DB
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv('DATABASE_URL') 
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html', title='Home', users=User.query.all())

    @app.route('/user', methods=['POST'])
    @app.route('/user/<name>', methods=['GET'])
    def user(name=None, message=''):
        name = name or request.values['user_name']
        try:
            if request.method == 'POST':
                add_user_twitter_scraper(name)
                message = "User {} successfully added!".format(name)
            tweets = User.query.filter(User.username == name).one().tweet
        except Exception as e:
            message = "Error adding {}: {}".format(name, e)
            tweets = []
        return render_template('user.html', title=name, tweets=tweets, message=message)

    @app.route('/compare', methods=['POST'])
    def compare(message=''):
        user1 = request.values['user1']
        user2 = request.values['user2']
        tweet_text = request.values['tweet_text']
        
        if user1 == user2:
            message = 'Cannot compare a user to themselves'
        else:
            prediction = predict_user(user1, user2, tweet_text)
            message = '"{}" is more likely to be said by {} than {}'.format(
                tweet_text, user1 if prediction else user2, user2 if prediction else user1
            )

        return render_template('prediction.html', title='Prediction', message=message)

    @app.route('/update', methods=['GET'])
    def update():
        update_all_users()
        return render_template('base.html', title='Prediction', users=User.query.all())

    # @app.route('/reset')
    # def reset():
    #     db.drop_all()
    #     db.create_all()
    #     return render_template('base.html', title='Reset Database!', users=User.query.all())


    return app

