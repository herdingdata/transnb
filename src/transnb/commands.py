import click

from transnb import messages


@click.command()
def tweet() -> None:
    """Entry point for sending a tweet."""
    print("do something")


@click.command()
def all_messages() -> list:
    return all()


def all():
    """all available messages"""
    return [m for m in messages.MESSAGES]
