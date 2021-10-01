import tweepy
import twitter_key
import re
import random


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

URL = input()
api = connect_api()

rt_count=int(input())

id= re.findall(r'/\d+', URL)[0][1:]
rt_list = api.retweets(id,200)


rt_lottery_list = random.sample(rt_list, rt_count)

for rt in rt_lottery_list:
    print(rt.user.screen_name)
