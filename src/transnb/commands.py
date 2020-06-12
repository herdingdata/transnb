import click
import tweepy

import settings as s
from transnb import messages


def _do_tweet():
    # msg = messages.get_random_message()
    msg = "Hello, world"  # debug
    click.echo(msg)

    auth = tweepy.OAuthHandler(s.API_KEY, s.API_SECRET_KEY)
    auth.set_access_token(s.ACCESS_TOKEN, s.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.update_status(msg)


@click.command()
def tweet() -> None:
    """Entry point for sending a tweet."""
    _do_tweet()


@click.command()
def all_messages() -> list:
    """all available messages"""
    for msg in messages.get_all_messages():
        click.echo(msg)


if __name__ == "__main__":
    _do_tweet()
