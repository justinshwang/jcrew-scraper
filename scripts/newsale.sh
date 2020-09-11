#!/bin/bash
# Filename: newsale.sh
# Description: 

usage() { echo -n "Usage: <action> [-h]" 1>&2; exit 1; }

cd ../jcrew
scrapy crawl filter | tail -1
# grep or tail output, send to test file

# execute random modules
cd ../modules
python3 test.py