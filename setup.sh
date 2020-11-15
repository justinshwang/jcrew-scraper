#!/bin/bash

sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev li
bffi-dev libssl-dev
sudo -i pip install scrapy

sudo apt purge -y python2.7-minimal
sudo ln -s /usr/bin/python3 /usr/bin/python

chmod u+x run.py
sudo apt-get install postfix

MINUTES="1"
HOURS="*"
HOMEDIR="/home/justinlongw"
PATH="/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin"

(crontab -l 2>/dev/null; echo "PATH=$PATH") | crontab -
(crontab -l 2>/dev/null; echo "*/$MINUTES $HOURS * * * . ~/.profile; cd $HOMEDIR/web-scraper && python run.py") | crontab -
