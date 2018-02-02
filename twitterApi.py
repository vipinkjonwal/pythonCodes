import twitter
from pprint import pprint
import tweepy

TOKEN = 'your token'
TOKEN_SECRET = 'your token secret'
CONSUMER = 'your consumer id'
CONSUMER_SECRET = 'your consumer secret'

auth = tweepy.OAuthHandler(CONSUMER,CONSUMER_SECRET)
url = auth.get_authorization_url()

api = tweepy.API(auth)

trends = api.trends_available()
print(trends[0])
