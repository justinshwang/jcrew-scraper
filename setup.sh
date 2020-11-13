#!/bin/bash

sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
sudo -i pip install scrapy

MINUTES="1"
HOURS="*"

(crontab -l 2>/dev/null; echo "*/$MINUTES $HOURS * * * /run.py") | crontab -
