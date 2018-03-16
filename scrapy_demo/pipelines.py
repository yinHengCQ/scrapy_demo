# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymssql


class HotelPipeline(object):
    def __init__(self):
        self.connect = pymssql.connect(host='192.168.1.163', user='sa', password='zx123456', database='RobotFliggy',charset='utf8')
        self.cursor = self.connect.cursor();

    def process_item(self, item, spider):
        self.cursor.execute("update hotelList set hotelName='{0}',hotelAddress='{1}',updateTime=getdate() where hotelId='{2}'".format(item['hotel_name'].encode('utf-8'),item['hotel_address'].encode('utf-8'),item['hotel_id']))
        self.cursor.execute("delete roomtypeList where hotelId={0}".format(item['hotel_id']))
        self.cursor.execute("delete roomtypePriceList where hotelId={0}".format(item['hotel_id']))
        self.cursor.execute(item['sql_roomtypeList'])
        self.cursor.execute(item['sql_roomtypePriceList'])
        self.connect.commit()
        return item


