import tweepy
import twitter_key

## 트위터 api와 연결
def connect_api():

    consumer_key = twitter_key.DATABASE_TWITTER_KEY['consumer_key']
    consumer_secret = twitter_key.DATABASE_TWITTER_KEY['consumer_secret']
    access_token = twitter_key.DATABASE_TWITTER_KEY['access_token']
    access_token_secret = twitter_key.DATABASE_TWITTER_KEY['access_token_secret']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    return api

    

account = "@niru_gom"
statuses = connect_api().user_timeline(screen_name=account, count=20)
print(statuses)


