import tweepy
from textblob import TextBlob

consumer_key = 'aIxPxbANbN7aIWmhgb9NOlL3h'
consumer_secret = 'BTL0DEIExSkSlCgTlPFBDTQ8IdOgOhkQwBNbiUO7dOkH9wCrfx'

access_token = '126535690-GoojeY3wBlY5HePpQnB6rCyGKRxyCDo6l8rNkoNT'
access_token_secret = 'TBxmJtXUq9QZbT0BaYjh32ihTqW1SdmDGNvJJkYBNaLo2'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Modi')

for tweet in public_tweets:
  print(tweet.text)
  analysis = TextBlob(tweet.text)
  print (analysis.sentiment)
