import tweepy

all_keys = open('Keys.txt','r').read().splitlines()
consumer_key = all_keys[0]
consumer_secret = all_keys[1]
access_token = all_keys[2]
access_token_secret = all_keys[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

api.update_status("Hello, Twitter!")

# pa = "Screenshot_8.png"
# api.media_upload(pa)


