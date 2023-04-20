import click
import tweepy

from settings import TWITTER
from transnb import messages, time


def do_tweet(message: str):
    if message is None:
        message = messages.get_random_message()
        do_a_post = time.do_i_post_a_tweet()
    else:
        # we got a message override so let's just post it regardless of probability
        do_a_post = True
    if do_a_post:
        auth = tweepy.OAuthHandler(TWITTER.API_KEY, TWITTER.API_SECRET_KEY)
        auth.set_access_token(TWITTER.ACCESS_TOKEN, TWITTER.ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        api.update_status(message)
        click.echo(f"transnb-tweet:posted:{message}")
    else:
        click.echo("transnb-tweet:skipped tweet")


@click.command()
@click.option("-m", "--message", default=None)
def tweet(*args, **kwargs) -> None:
    """Entry point for sending a tweet."""
    _do_tweet(*args, **kwargs)


if __name__ == "__main__":
    _do_tweet()
