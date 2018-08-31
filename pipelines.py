# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
from scrapyTest.items import TlCygItem
from scrapyTest.items import equipWuHun


class ScrapytestPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, equipWuHun):
            col_name_list = spider.roleEquipWuHun_columns
            self.updRoleData('roleEquipWuHun',item ,spider.roleEquipWuHun_columns)
        else:
            col_name_list = spider.roleinfo_columns
            self.updRoleData('cyg_roleinfo', item, spider.roleinfo_columns)

    def genValueAndParamList(self, item, col_name_list, valuelist, paramlist):
        for column in col_name_list:
            valuelist.append('?')
            paramlist.append(item[column])
        valuestr = ",".join(valuelist)
        columnstr = ",".join(col_name_list)
        return  valuestr, columnstr

    def updRoleData(self, tableName, item, col_name_list):
        valuelist = []
        paramlist = []
        valuestr, columnstr = self.genValueAndParamList(item, col_name_list, valuelist, paramlist)
        conn = sqlite3.connect('scrapyTest/roleinfo.sqlite')
        c = conn.cursor()
        sqlstr = "select url from "+tableName+" where url = ?"
        c.execute(sqlstr, (item['url'],))
        url = c.fetchall()
        if url:
            updsql = "UPDATE "+tableName+" SET "
            delimiter = ""
            for column in col_name_list:
                updsql += delimiter
                updsql += column+"=?"
                delimiter=" , "
            if delimiter:
                updsql += " where url=?"
                paramlist.append(item['url'])
                c.execute(updsql, paramlist)
                conn.commit()
        else:
            insql = "INSERT INTO "+tableName+" ({}) VALUES ({})".format(columnstr, valuestr)
            c.execute(insql, paramlist)
            conn.commit()
        c.close()
        conn.close()
