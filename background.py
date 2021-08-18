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

api = connect_api()
id=0
rt_count = 15
rt_list = api.retweets(id, rt_count)

for rt in rt_list:
    print(rt.user.screen_name)
