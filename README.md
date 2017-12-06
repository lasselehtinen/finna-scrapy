# Installation
 1. Install Python
 2. Install Scrapy
 3. Install ElasticSearch pipeline to Scrapy (pip install ScrapyElasticSearch)
 4. Clone this git repo

# Important files
### finna/items.py
Holds the definition for the Finna items.

    import scrapy
    
    class FinnaItem(scrapy.Item):
        id = scrapy.Field()
        title = scrapy.Field()
        formats = scrapy.Field()
        images = scrapy.Field()
        nonPresenterAuthors = scrapy.Field()
        subjects = scrapy.Field()
        year = scrapy.Field()
        pass

### finna/spiders/items.py
The actual scraper. Does the pagination and makes a request per page to the Finna API. Loops through each record in the response and checks if the given field exists.

# Running scraper
    scrapy crawl items
