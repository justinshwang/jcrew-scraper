# scraper
Web scraper using Python Scrapy Library. Uses cron to run scheduled script on linux machine.

## Setup

1. Windows
```
pip install Scrapy 
```
2. Linux
All dependencies installed running setup.sh along with cron setup 


## Run program
Schedule a Cron Job (Linux Only)
1. Run setup.sh script. Modify HOUR, MINUTE, and PATH variables in script to schedule when spider appropriately
```
bash setup.sh
```
This also installs necessary dependencies...

Manually
1. Run the run.py file to manually crawl spider(s)
```
python3 run.py
```


# Development
1. Add a new spider
- Add SPIDERNAME.py file in jcrew/jcrew/spiders/ directory
- Add script to setup.sh to run as cron job

## Run a Spider
1. cd into directory of spiders
2. Run the following command
```
scrapy crawl <name-of-spider>
```

## Nifi (ops Branch Only)
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
