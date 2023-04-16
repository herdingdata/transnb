import click
import tweepy_mastodon as tweepy

import settings as s
from transnb import messages, time


def _do_toot(message: str):
    if message is None:
        message = messages.get_random_message()
        do_a_post = time.do_i_post_a_toot()
    else:
        # we got a message override so let's just post it regardless of probability
        do_a_post = True
    if do_a_post:
        api = get_mastodon_api()
        api.update_status(message)
        click.echo(f"transnb-toot:posted:{message}")
    else:
        click.echo("transnb-toot:skipped toot")


def get_mastodon_api():
    """
    grab the auth credentials from settings & set up a working API
    """
    auth = tweepy.OAuth1UserHandler(consumer_key=s.CLIENT_KEY, consumer_secret=s.CLIENT_SECRET, api_base_url=s.BASE_URL)
    auth.set_access_token(s.ACCESS_TOKEN)
    return tweepy.API(auth)


@click.command()
@click.option("-m", "--message", default=None)
def toot(*args, **kwargs) -> None:
    """Entry point for sending a toot."""
    _do_toot(*args, **kwargs)


@click.command()
def all_messages():
    """all available messages"""
    for msg in messages.get_all_messages():
        click.echo(msg)


@click.command()
def analyse():
    """stats about how the app behaves"""
    time.analyse()


if __name__ == "__main__":
    _do_toot()
