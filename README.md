![logo by @smolrobots](logo.png "Logo by @smolrobots")
# Trans & NB Solidarity bot

A bot which sends messages of love and solidarity to our
trans and non-binary friends in the LGBTQ+ community.

This repo is the code which powers [@transnb@botsin.space](https://botsin.space/@transnb)
which used to live on twitter [@transnb](https://twitter.com/transnb).

- Project created with love by [Andy Herd](https://herdingdata.co.uk) (he/him)
- Andy is`@herdingdata` on [mastodon](https://mastodon.scot/@herdingdata) & [twitter](https://twitter.com/herdingdata)
- If you want to support me, I would welcome a donation to my climate action & conservation charity
[Protect Earth](https://www.protect.earth/)
- The beautiful bot logo was created by [@smolrobots](https://twitter.com/smolrobots)
who you can support on [patreon](https://www.patreon.com/thomasheasmanhunt)

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

## Commands
```
# Do a tweet of a randomly picked predefined message
transnb-tweet

# Do a tweet and choose a specific message
transnb-tweet -m "message goes here"
# or
transnb-tweet --message "message goes here"

# Show all the messages
transnb-all
```

## Other stuff
Message for future Andy: you'll probably need these links the next time you look at this project.
- http://docs.tweepy.org/en/latest/api.html#api-reference
- https://developer.twitter.com/en/apps

## Raspberry pi
For making it run on a schedule.

https://installvirtual.com/how-to-install-python-3-8-on-raspberry-pi-raspbian/

```
# prerequisites
sudo apt-get update
sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev tar wget vim

# get python
cd /home/USERNAMEHERE
wget https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz
sudo tar zxf Python-3.8.3.tgz

# install
cd Python-3.8.3
sudo ./configure --enable-optimizations
sudo make -j 4
sudo make altinstall

# tidy up
cd ..
sudo rm -rf Py*

# virtualenv
sudo python3.8 -m pip install virtualenvwrapper
mkdir -p ~/.virtualenvs
echo 'export WORKON_HOME=$HOME/.virtualenvs' >> ~/.bash_profile
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bash_profile
source ~/.bash_profile

# now our code
git clone git@github.com:herdingdata/transnb.git
cd transnb
make setup
# don't forget the credentials in settings.py

make test



# Open the crontab in edit mode
crontab -e

*/7 * * * * /path/to/.virtualenv/transnb/bin/transnb-tweet | logger

```

PS here's some mastodon verification <a rel="me" href="https://botsin.space/@transnb">mastodon verification</a>
