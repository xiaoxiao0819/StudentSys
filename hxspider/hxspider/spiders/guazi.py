# -*- coding: utf-8 -*-
import scrapy


class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['www.guazi.com/cd/']
    start_urls = ['http://www.guazi.com/cd//']

    def parse(self, response):
        print(response)
