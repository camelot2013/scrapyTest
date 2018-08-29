# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class ScrapytestPipeline(object):
    def process_item(self, item, spider):
        conn = sqlite3.connect('scrapyTest/roleinfo.sqlite')
        c = conn.cursor()
        col_name_list = spider.col_name_list
        valuelist = []
        paramlist = []
        for column in col_name_list: #python2.7的list对象没有copy方法,用遍历的方式生成副本list
            valuelist.append('?')
            paramlist.append(item[column])
        valuestr = ",".join(valuelist)
        columnstr = ",".join(col_name_list)
        insql = "INSERT INTO cyg_roleinfo ({}) VALUES ({})".format(columnstr,valuestr)
        c.execute(insql,paramlist)
        conn.commit()
        conn.close()
