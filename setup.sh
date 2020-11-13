#!/bin/bash

(crontab -l 2>/dev/null; echo "*/* * * * * /run.py") | crontab -
