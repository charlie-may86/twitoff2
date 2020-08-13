# core funtionality to add users
from os import getenv
import basilica
from twitter_scraper import get_tweets, Profile
from .db_model import db, User, Tweet
from dotenv import load_dotenv

load_dotenv()

BASILICA = basilica.Connection(getenv('BASILICA_KEY'))

def add_user_twitter_scraper(username):
    """Add a user and their tweets to database."""
    try:
        # Get user profile   
        user_profile = Profile(username)
        
        # Add to User table (or check if existing)
        db_user = (User.query.get(user_profile.user_id) or
                   User(id=user_profile.user_id,
                        username=username))
        db.session.add(db_user)


        # Get tweets ignoring re-tweets and replies
        tweets = list(get_tweets(username, pages=25))
        original_tweets = [tweet for tweet in tweets if tweet['username']==username]


        # # Add newest_tweet_id to the User table
        # if tweets:
        #     db_user.newest_tweet_id = tweets[0].id
    
        # Loop over tweets, get embedding and add to Tweet table
        for tweet in tweets:

            # Get an examble basilica embedding for first tweet
            embedding = BASILICA.embed_sentence(tweet['text'], model='twitter')

            # Add tweet info to Tweet table
            db_tweet = Tweet(id=tweet['tweetId'],
                             text=tweet['text'][:300],
                             embedding=embedding)
            db_user.tweet.append(db_tweet)
            db.session.add(db_tweet)

            
    except Exception as e:
        print('Error processing {}: {}'.format(username, e))
        raise e

    else:
        db.session.commit()

    def update_all_users():
        '''Update all tweets for all Users in the User Table'''
        for user in User.query.all():
            add_user_twitter_scraper()