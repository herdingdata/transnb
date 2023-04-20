from dataclasses import dataclass


@dataclass(frozen=True)
class _MastodonConfig:
    CLIENT_KEY: str
    CLIENT_SECRET: str
    ACCESS_TOKEN: str
    BASE_URL: str


@dataclass(frozen=True)
class _TwitterConfig:
    API_KEY: str
    API_SECRET_KEY: str
    ACCESS_TOKEN: str
    ACCESS_TOKEN_SECRET: str


MASTODON = _MastodonConfig(
    CLIENT_KEY="REPLACEME",
    CLIENT_SECRET="REPLACEME",
    ACCESS_TOKEN="REPLACEME",
    BASE_URL="botsin.space",
)


TWITTER = _TwitterConfig(
    API_KEY="REPLACEME",
    API_SECRET_KEY="REPLACEME",
    ACCESS_TOKEN="REPLACEME",
    ACCESS_TOKEN_SECRET="REPLACEME",
)
