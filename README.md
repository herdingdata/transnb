![logo by @smolrobots](logo.png "Logo by @smolrobots")
# Trans & NB Solidarity bot

A bot which sends messages of love and solidarity to our
trans and non-binary friends in the LGBTQ+ community.

This repo is the code which powers [@transnb](https://twitter.com/transnb)

Project created with love by [Andy Herd](https://herdingdata.co.uk) (twitter [@herdingdata](https://twitter.com/herdingdata))

The beautiful bot logo was created by [@smolrobots](https://twitter.com/smolrobots)

## First time setup (development)
```
# Create virtualenv with py3.8 (your command may vary)
mkvirtualenv transnb -p /usr/local/bin/python3.8

# Create credentials file
cp src/settings_local.py src/settings.py

# Then put the auth details into src/settings.py
vi src/settings.py

make setup
make install-git-hooks
make test
```

## First time setup (server)
Do the steps above on a server which you want to post tweets regularly. Then:

```
# Open the crontab in edit mode
crontab -e

TODO zomg there's more to figure out
```

## Commands
```
# Do a tweet of a randomly picked predefined message
transnb-tweet

# Show all the messages
transnb-all
```

## Other stuff
Message for future Andy: you'll probably need these links the next time you look at this project.
- http://docs.tweepy.org/en/latest/api.html#api-reference
- https://developer.twitter.com/en/apps
