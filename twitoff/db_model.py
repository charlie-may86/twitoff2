'''SQLAlchemy models for Twitoff'''
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    # follower_count = db.Column(db.Integer, nullable=False)
    # tweet IDS are ordinal ints, so we can fetch most recent tweets
    # newest_tweet_id = db.Column(db.BigInteger, nullable=False)


    # called a dunder method prints the user name when you refernce the user
    def __repr__(self):
        return '<User %r>' % self.username

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Unicode(300))
    embedding = db.Column(db.PickleType, nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False) 
    user = db.relationship('User', backref=db.backref('tweet', lazy=True))


    # called a dunder method prints the user name when you refernce the user
    def __repr__(self):
        return '<Tweet %r>' % self.text