# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class HotelItem(scrapy.Item):
    hotel_id=scrapy.Field()
    hotel_name=scrapy.Field()
    hotel_address=scrapy.Field()
    sql_roomtypeList=scrapy.Field()
    sql_roomtypePriceList=scrapy.Field()