# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class ScrapytestPipeline(object):
    def process_item(self, item, spider):
        # print item
        conn = sqlite3.connect('scrapyTest/roleinfo.sqlite')
        c = conn.cursor()
        # c.execute(
        #     "INSERT INTO cyg_roleinfo (charName,sex,menpai,level,price,gemNum3,gemNum4,gemNum5,gemNum6,gemNum7,gemNum8,gemNum9,equipScore,xinFaScore,xiuLianScore,gemXiuLianScore,maxHp,maxMp,str,strPlus,spr,sprPlus,con,conPlus,com,comPlus,dex,dexPlus,hit,hitPlus,miss,missPlus,criticalAtt,criticalDef,coldAtt,coldDef,resistColdDef,resistColdDefLimit,fireAtt,fireDef,resistFireDef,resistFireDefLimit,lightAtt,lightDef,resistLightDef,resistLightDefLimit,postionAtt,postionDef,resistPostionDef,resistPostionDefLimit,chuanCiShangHai,chuanCiJianMian) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        #     (item['charName'], item['sex'], item['menpai'], item['level'], item['price'], item['gemNum3'],
        #      item['gemNum4'], item['gemNum5'], item['gemNum6'], item['gemNum7'], item['gemNum8'], item['gemNum9'],
        #      item['equipScore'], item['xinFaScore'],
        #      item['xiuLianScore'], item['gemXiuLianScore'], item['maxHp'], item['maxMp'], item['str'], item['strPlus'],
        #      item['spr'], item['sprPlus'], item['con'], item['conPlus'], item['com'], item['comPlus'], item['dex'],
        #      item['dexPlus'], item['hit'], item['hitPlus'], item['miss'], item['missPlus'], item['criticalAtt'],
        #      item['criticalDef'], item['coldAtt'], item['coldDef'], item['resistColdDef'], item['resistColdDefLimit'],
        #      item['fireAtt'], item['fireDef'], item['resistFireDef'], item['resistFireDefLimit'], item['lightAtt'],
        #      item['lightDef'], item['resistLightDef'], item['resistLightDefLimit'], item['postionAtt'],
        #      item['postionDef'], item['resistPostionDef'], item['resistPostionDefLimit'], item['chuanCiShangHai'],
        #      item['chuanCiJianMian']));
        # conn.commit()
        # c.execute('PRAGMA table_info(cyg_roleinfo)')
        # cyg_roleinfo = c.fetchall()
        # for columnid, columnname in cyg_roleinfo:
        #     print columnid,columnname
        # c.execute("SELECT * FROM {}".format('cyg_roleinfo'))
        # col_name_list = [tuple[0] for tuple in c.description]
        col_name_list = spider.col_name_list
        valuelist = []
        paramlist = []
        for column in col_name_list: #python2.7的list对象没有copy方法,用遍历的方式生成副本list
            valuelist.append('?')
            paramlist.append(item[column])
        valuestr = ",".join(valuelist)
        columnstr = ",".join(col_name_list)
        insql = "INSERT INTO cyg_roleinfo ({}) VALUES ({})".format(columnstr,valuestr)
        # print insql
        c.execute(insql,paramlist)
        conn.commit()
        conn.close()
