# scraper
Web scraper using Python Scrapy Library and argparse for parser. Utilizing argparse for CLI.

## Setup

Install required libraries
```
pip install -r requirements.txt
```


Run the playbook playbook_ansible.yml. This one will get all the roles and put them in roles/ sub-directory 
```
ansible-playbook -i hosts playbook_ansible.yml
```
Run the actual playbook playbook_scrapy.yml in order to provision the server.
```
ansible-playbook -i hosts playbook_scrapy.yml
```

## Run program
1. Run the parser.py file with arguments or -h flag for help
```
python parser.py <function_name> [arg_one] [arg_two] [-h]
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


# Development
1. Add a new spider
    a. Add SPIDERNAME.py file in jcrew/jcrew/spiders/ directory
    b. Add script to scripts/ directory 
