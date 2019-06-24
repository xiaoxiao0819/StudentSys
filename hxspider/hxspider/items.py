# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GuaziItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = 'guazi'
    buy_year = scrapy.Field()
    run = scrapy.Field()
    intro = scrapy.Field()
    sale = scrapy.Field()
    old_sale = scrapy.Field()
