# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    date = scrapy.Field()
    volume = scrapy.Field()
    high = scrapy.Field()
    low	= scrapy.Field()
    last_traded_price = scrapy.Field()
    prev_price = scrapy.Field()
    change = scrapy.Field()
