# core funtionality to add users
from os import getenv
import basilica
import twitter_scrapper
from .db_model import db, User, Tweet
from dotenv import load_dotenv

load_dotenv()

BASILICA = basilica.Connection(getenv('BASILICA_KEY'))

def add_user_twitter_scraper(username):
    """Add a user and their tweets to database."""
    try:
        # Get user profile   
        user_profile = list(get_tweets(username, pages=25))
        
        # Add to User table (or check if existing)
        db_user = (User.query.get(twitter_user.id) or
                   User(id=twitter_user.id,
                        username=username,
                        follower_count=twitter_user.followers_count))
        db.session.add(db_user)


        # Get tweets ignoring re-tweets and replies
        tweets = twitter_user.timeline(count=200,
                                       exclude_replies=True,
                                       include_rts=False,
                                       tweet_mode='extended',
                                       since_id=db_user.newest_tweet_id)

        # Add newest_tweet_id to the User table
        if tweets:
            db_user.newest_tweet_id = tweets[0].id
    
        # Loop over tweets, get embedding and add to Tweet table
        for tweet in tweets:

            # Get an examble basilica embedding for first tweet
            embedding = BASILICA.embed_sentence(tweet.full_text, model='twitter')

            # Add tweet info to Tweet table
            db_tweet = Tweet(id=tweet.id,
                             text=tweet.full_text[:300],
                             embedding=embedding)
            db_user.tweet.append(db_tweet)
            db.session.add(db_tweet)

            
    except Exception as e:
        print('Error processing {}: {}'.format(username, e))
        raise e

    return original_tweets, embedding
