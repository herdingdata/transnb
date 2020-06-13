import click
import tweepy

import settings as s
from transnb import messages
from transnb.time import do_i_post_a_tweet


def _do_tweet():
    if do_i_post_a_tweet() is True:
        msg = messages.get_random_message()
        click.echo(f"transnb-tweet:posted:{msg}")
        auth = tweepy.OAuthHandler(s.API_KEY, s.API_SECRET_KEY)
        auth.set_access_token(s.ACCESS_TOKEN, s.ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        api.update_status(msg)
    else:
        click.echo("transnb-tweet:skipped tweet")


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
