import os
from twython import Twython


consumer_key        = os.environ.get('TW_CON_KEY')
consumer_secret     = os.environ.get('TW_CON_SECRET')
access_token        = os.environ.get('TW_ACCS_TOK')
access_token_secret = os.environ.get('TW_TOK_SCRT')


def tweet(message):
    twitter = Twython(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )
    twitter.update_status(status=message)
