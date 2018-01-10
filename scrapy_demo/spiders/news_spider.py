# -*- coding: utf-8 -*-
import scrapy
from scrapy_demo.items import NewsItem


class NewsSpiderSpider(scrapy.Spider):
    name = 'news_spider'
    allowed_domains = ['business.sohu.com']
    start_urls = ['http://business.sohu.com/']

    def parse(self, response):
        # news=response.xpath('//div[@class="news-wrapper"]/div[@class="news-box clear   news-box-aa "]')
        news=response.xpath('//div[@data-role="news-item"]/h4/a/text()')
        for var in news:
            # item=NewsItem()
            # item['title']=var.xpath('./h4/a/text()').extract()[0]
            # yield item
            print '*'*100
            print var.extract()
