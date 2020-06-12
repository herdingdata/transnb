import tweepy

import settings as s


def test__can_see_twitter():
    # basically do we have valid credentials?
    auth = tweepy.OAuthHandler(s.API_KEY, s.API_SECRET_KEY)
    auth.set_access_token(s.ACCESS_TOKEN, s.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    result = api.me()

    assert result.screen_name == "transnb"
