# scraper
Web scraper using Python Scrapy Library and argparse for parser. 

## Setup

Install required libraries
```
pip install -r requirements.txt
```

## Run program
1. Run the parser.py file with arguments or -h flag for help
```
python parser.py <function_name> [arg_one] [arg_two] [-h]
```

# Development
1. Add a new spider
    a. Add SPIDERNAME.py file in amazon/amazon/spiders/ directory
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

