# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FinnaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    formats = scrapy.Field()
    images = scrapy.Field()
    nonPresenterAuthors = scrapy.Field()
    subjects = scrapy.Field()
    year = scrapy.Field()
    pass
