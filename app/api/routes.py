from fastapi import APIRouter
from typing import List
from app.function.tagSearch import getDataFromHashTag
from fastapi.responses import JSONResponse
# import getDataFromHashTag from app.function.tagSearch
import tweepy

router = APIRouter()

# if path api is index or default return html page say greeting

@router.get('/')
async def index():
    return {'message': 'Hello, World!'}
    

@router.get('/hello')
async def hello():
    return {'message': 'Hello, World!'}


@router.get("/users/me")
async def get_user_info(
    api_key: str = "ZgY7EmuqNBzbEghNB1SWEHII6",
    api_key_secret: str = "zWvbEn3jvkcVsvQcfCoHV3uLedMHoWwD8UeKlpk5z38d7g8SVr",
    access_token: str = "1576002791633346560-rnBTiYRlPYspSPY3V5jv5otl2555V7",
    access_token_secret: str = "6LvSZjRdy8HWrh2ONmlmVrtGZSqjvsenZ6DciQtQgEqxS",
):
    try:
        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)

      # Create the API object
        api = tweepy.API(auth)
        user = api.verify_credentials()
        response = {
            "id": user.id_str,
            "name": user.name,
            "username": user.screen_name,
            "description": user.description,
            "location": user.location,
            "url": user.url,
            "followers_count": user.followers_count,
            "friends_count": user.friends_count,
            "statuses_count": user.statuses_count,
        }
        return JSONResponse(content=response)
    except tweepy.TweepError as error:
        return JSONResponse(content={"error": str(error)})

@router.get("/users/me/tweets")
async def get_user_tweets(
    api_key: str = "ZgY7EmuqNBzbEghNB1SWEHII6",
    api_key_secret: str = "zWvbEn3jvkcVsvQcfCoHV3uLedMHoWwD8UeKlpk5z38d7g8SVr",
    access_token: str = "1576002791633346560-rnBTiYRlPYspSPY3V5jv5otl2555V7",
    access_token_secret: str = "6LvSZjRdy8HWrh2ONmlmVrtGZSqjvsenZ6DciQtQgEqxS",
):
    try:
        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)

      # Create the API object
        api = tweepy.API(auth)
        user = api.verify_credentials()
        tweets = api.user_timeline(id=user.id_str, count=100, tweet_mode="extended")
        response = {
            "tweets": [
                {
                    "id": tweet.id_str,
                    "text": tweet.full_text,
                    "created_at": tweet.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                    "retweet_count": tweet.retweet_count,
                    "favorite_count": tweet.favorite_count,
                    "lang": tweet.lang,
                }
                for tweet in tweets
            ]
        }
        return JSONResponse(content=response)
    except tweepy.TweepError as error:
        return JSONResponse(content={"error": str(error)})

# Define the hashtag you want to search for
# hashtag = '#example'

@router.get('/tweet/{hashtag}')
async def get_tweets(
    hashtag : str,
    api_key: str = "ZgY7EmuqNBzbEghNB1SWEHII6",
    api_key_secret: str = "zWvbEn3jvkcVsvQcfCoHV3uLedMHoWwD8UeKlpk5z38d7g8SVr",
    access_token: str = "1576002791633346560-rnBTiYRlPYspSPY3V5jv5otl2555V7",
    access_token_secret: str = "6LvSZjRdy8HWrh2ONmlmVrtGZSqjvsenZ6DciQtQgEqxS",
):

    # print("herer1")

    # auth = tweepy.OAuthHandler(kwargs["api_key"], kwargs["api_key_secret"])
    # auth.set_access_token(
    #     kwargs["access_token"],
    #     kwargs["access_token_secret"]
    #     )

    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

      # Create the API object
    api = tweepy.API(auth)

    # Use the API to search for tweets containing the hashtag
    tweets = []
    for tweet in tweepy.Cursor(api.get_user, q=hashtag, tweet_mode='extended').items(10):
        tweets.append(tweet.full_text)

    # Return the list of tweet texts as JSON
    return {'tweets': tweets}
    # type = type(tweets)
    # obj = { id:number, name:string content:string, date:string, tag:string[] }



# @router.get('/tweets/{hashtag}', response_model=List[str])
# async def search_hashtag(hashtag: str):
#     try:
#        data = getDataFromHashTag(hashtag)

#        return data

#     except Exception as e:
#         return {'error': str(e)}


# @router.get('/tweetsTag/{hashtag}')
# async def search_hashtag(hashtag: str):
#     return {'message': f"Hello, {hashtag}"}

