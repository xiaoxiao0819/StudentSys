# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from hxspider.hxspider.items import GuaziItem


class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    # allowed_domains = 'guazi.com/cd/buy/o1/#bread'
    # start_urls = 'http://https://www.guazi.com/cd/buy/o1/#bread/'

    def start_requests(self):
        for page in range(1,51):
            url = 'https://www.guazi.com/cd/buy/o{}/#bread'.format(page)
            yield Request(url,callback=self.parse, dont_filter=True)

    def parse(self, response):
        # print(response.text)
        cars = response.xpath('/html/body/div[6]/ul/li')
        print('='*30)
        # print(cars)
        for car in cars:
            item = GuaziItem()
            item['buy_year']=car.xpath('./a/div[1]/text()[1]').extract_first().strip()
            item['run']=car.xpath('./a/div[1]/text()[2]').extract_first().strip()
            item['intro']=car.xpath('./a/h2/text()').extract_first().strip()
            item['sale']=car.xpath('./a/div[2]/p/text()[1]').extract_first().strip()+'万'
            item['old_sale']=car.xpath('./a/div[2]/em/text()').extract_first()
            print('=='*50)
            yield item
