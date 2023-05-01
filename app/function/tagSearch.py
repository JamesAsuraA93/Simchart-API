import tweepy

def getDataFromHashTag(text:str):
  

    auth = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret, access_token, access_token_secret
    )

    api = tweepy.API(auth)

    tweets = []
    for tweet in tweepy.Cursor(api.search_tweets, q=text, tweet_mode='extended').items(10):
        tweets.append(tweet.full_text)

    return tweets