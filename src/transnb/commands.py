import click
import tweepy

import settings as s
from transnb import messages
from transnb.time import do_i_post_a_tweet


def _do_tweet(message: str):
    if message is None:
        message = messages.get_random_message()
        do_a_post = do_i_post_a_tweet()
    else:
        # we got a message override so let's just post it regardless of probability
        do_a_post = True
    if do_a_post:
        auth = tweepy.OAuthHandler(s.API_KEY, s.API_SECRET_KEY)
        auth.set_access_token(s.ACCESS_TOKEN, s.ACCESS_TOKEN_SECRET)
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


@click.command()
def all_messages() -> list:
    """all available messages"""
    for msg in messages.get_all_messages():
        click.echo(msg)


if __name__ == "__main__":
    _do_tweet()
