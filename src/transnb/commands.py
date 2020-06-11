import click


@click.command()
def tweet() -> None:
    """Entry point for sending a tweet."""
    print("do something")


@click.command()
def all() -> None:
    """Print all available messages."""
    print("do something")
