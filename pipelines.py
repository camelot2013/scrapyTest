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
        for column in col_name_list:
            valuelist.append('?')
            paramlist.append(item[column])
        valuestr = ",".join(valuelist)
        columnstr = ",".join(col_name_list)
        # sqlstr = "select url from cyg_roleinfo where url = ?"
        # c.execute(sqlstr, (item['url'],))
        # url = c.fetchall()
        # if url:
        #     #UPDATE的规则还没想好
        #     # print url
        #     updsql = "UPDATE cyg_roleinfo SET "
        #     delimiter=""
        #     for column in col_name_list:
        #         updsql += delimiter
        #         updsql += column+"=?"
        #         delimiter=" , "
        #     if delimiter:
        #         updsql +=" where url=?"
        #         paramlist.append(item['url'])
        #         c.execute(updsql,paramlist)
        #         conn.commit()
        # else:
        #     insql = "INSERT INTO cyg_roleinfo ({}) VALUES ({})".format(columnstr, valuestr)
        #     c.execute(insql, paramlist)
        #     conn.commit()
        insql = "INSERT INTO cyg_roleinfo ({}) VALUES ({})".format(columnstr, valuestr)
        c.execute(insql, paramlist)
        conn.commit()
        conn.close()
