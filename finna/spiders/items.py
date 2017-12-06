# -*- coding: utf-8 -*-
import scrapy
import json
from finna.items import FinnaItem

class ItemsSpider(scrapy.Spider):
    name = 'items'
    allowed_domains = ['api.finna.fi']
    start_urls = ['https://api.finna.fi/api/v1/search?filter[]=format:"0/Book/"&field[]=formats&field[]=id&field[]=images&field[]=nonPresenterAuthors&field[]=subjects&field[]=title&field[]=year&limit=100&page=%s' % page for page in xrange(1,60828)]

    def parse(self, response):

        jsonresponse = json.loads(response.body_as_unicode())

        items = []

        fields = ['id', 'title', 'formats', 'images', 'nonPresenterAuthors', 'subjects', 'year']

        for record in jsonresponse["records"]:
           item = FinnaItem()

           for field in fields:
                if field in record:
                        item[field] = record[field]

           items.append(item)
        return items

