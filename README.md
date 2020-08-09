# jcrew-scraper
Web Scraper for J.Crew website using Nifi and Scrapy

## Setup

Install required libraries
```
pip install -r requirements.txt
```

# TODO List

1. Scraper
    a. Detect when first four sale items when sorted by "newest to sale" change
    b. For now, store item html data to MongoDB (?) or just html file
2. Nifi Setup
    a. Connect any additional processers, basic setup with scraper added to each node
    b. Send email alert when first four sale items change
3. Additional
    a. Setup NiFi as a windows service
    b. Additional support to Nifi
    c. Detect when a new item has been added that has never been added before (store in database) -- not necessarily
    labeled "new to sale". Suggest these items or 'good deals' i.e. scarce items with new low prices