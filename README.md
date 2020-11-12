# scraper
Web scraper using Python Scrapy Library. Uses cron to run scheduled script on linux machine.

## Setup

Install required libraries
```
pip install -r requirements.txt
```


## Run program
1. Run the run.py file. Run cron to schedule this periodically
```
python library/run.py
```

# Development
1. Add a new spider
    a. Add SPIDERNAME.py file in jcrew/jcrew/spiders/ directory
    b. Add script to scripts/ directory 


## Run a Spider
1. cd into directory of spiders
2. Run the following command
```
scrapy crawl <name-of-spider>
```

## Nifi (Dev-Ops Branch Only)
    Cluster Manager - Port 11000
    node1 - Port 11001
    node1 - Port 11002

## Ansible
    Run the playbook playbook_ansible.yml. This one will get all the roles and put them in roles/ sub-directory 
    ```
    ansible-playbook -i hosts playbook_ansible.yml
    ```
    Run the actual playbook playbook_scrapy.yml in order to provision the server.
    ```
    ansible-playbook -i hosts playbook_scrapy.yml
    ```
