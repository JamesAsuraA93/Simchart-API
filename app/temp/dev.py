import tweepy
import os
import sys
import geocoder


def get_api(**kwargs):
    """Gets the API object after authorization
    and authentication.
    :keyword api_key: The consumer API key.
    :keyword api_key_secret: The consumer API key secret.
    :keyword access_token: The access token.
    :keyword access_token_secret: The access token secret.
    :returns: The Tweepy API object.
    """
    auth = tweepy.OAuthHandler(kwargs["api_key"], kwargs["api_key_secret"])
    auth.set_access_token(
        kwargs["access_token"],
        kwargs["access_token_secret"]
        )
    return tweepy.API(auth)


def get_trends(api, loc):
    """Gets the trending search results from Twitter.
    :param api: The Tweepy API object.
    :param loc: The location to search for.
    :returns: A dictionary of trending search results.
    """
    # Get available locations that have trends.
    # available_loc = api.available_trends()

    # Object that has location's latitude and longitude.
    g = geocoder.osm(loc)

    closest_loc = api.closest_trends(g.lat, g.lng)
    trends = api.get_place_trends(closest_loc[0]["woeid"])
    return trends[0]["trends"]


def extract_hashtags(trends):
    """Extracts the hashtags from the trending search results.
    :param trends: A list of trending search results.
    :returns: A lisselft of hashtags.
    """
    hashtags = [trend["name"] for trend in trends if "#" in trend["name"]]
    return hashtags


def get_n_tweets(api, hashtag, n, lang=None):
    """Gets the n tweets of the trending hashtag.
    :param api: The Tweepy API object.
    :param hashtag: The trending hashtag.
    :param n: The number of tweets to get.
    :returns: A string of the status.
    """
    for status in tweepy.Cursor(
        api.search_tweets,
        q=hashtag,
        lang=lang
    ).items(n):
        print(f"https://twitter.com/i/web/status/{status.id}")


if __name__ == "__main__":
    API_KEY = "ZgY7EmuqNBzbEghNB1SWEHII6"
    API_Key_Secret = "zWvbEn3jvkcVsvQcfCoHV3uLedMHoWwD8UeKlpk5z38d7g8SVr"
    Access_Token = "1576002791633346560-rnBTiYRlPYspSPY3V5jv5otl2555V7"
    Access_Token_Secret = "6LvSZjRdy8HWrh2ONmlmVrtGZSqjvsenZ6DciQtQgEqxS"
    
    api = get_api(
        api_key=API_KEY,
        api_key_secret=API_Key_Secret,
        access_token=Access_Token,
        access_token_secret=Access_Token_Secret
    )
    # Pass an argument for the location e.g. Egypt
    loc = sys.argv[1]
    trends = get_trends(api, loc)
    hashtags = extract_hashtags(trends)
    for hashtag in hashtags:
        print(hashtag)
    hashtag = hashtags[0]
    status = get_n_tweets(api, hashtag, 5, "ar")