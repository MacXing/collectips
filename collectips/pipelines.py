# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class CollectipsPipeline(object):

    def process_item(self, item, spider):
        database = spider.setting.get('DATABASE')
        conn = pymysql.connect(database)
        cursor = conn.cursor()
        sql = ("INSERT INTO proxy_ip(ip,port,address,position,type,valide_time)"
               "VALUES(%s,%s,%s,%s,%s,%s)")
        lis=(item['ip'],item['port'],item['address'],item['position'],item['type'],item['valide_time'])
        try:
            cursor.execute(sql,lis)
        except:
            print(lis)
        else:
            conn.commit()
        cursor.close()
        conn.close()
        return item

