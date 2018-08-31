# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TlCygItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    charName = scrapy.Field()
    sex = scrapy.Field()
    menpai = scrapy.Field()
    level = scrapy.Field()
    price = scrapy.Field()
    gemNum3 = scrapy.Field()
    gemNum4 = scrapy.Field()
    gemNum5 = scrapy.Field()
    gemNum6 = scrapy.Field()
    gemNum7 = scrapy.Field()
    gemNum8 = scrapy.Field()
    gemNum9 = scrapy.Field()
    equipScore = scrapy.Field()
    xinFaScore = scrapy.Field()
    xiuLianScore = scrapy.Field()
    gemXiuLianScore = scrapy.Field()
    maxHp = scrapy.Field()
    maxMp = scrapy.Field()
    str = scrapy.Field()
    strPlus = scrapy.Field()
    spr = scrapy.Field()
    sprPlus = scrapy.Field()
    con = scrapy.Field()
    conPlus = scrapy.Field()
    com = scrapy.Field()
    comPlus = scrapy.Field()
    dex = scrapy.Field()
    dexPlus = scrapy.Field()
    hit = scrapy.Field()
    hitPlus = scrapy.Field()
    miss = scrapy.Field()
    missPlus = scrapy.Field()
    criticalAtt = scrapy.Field()
    criticalDef = scrapy.Field()
    coldAtt = scrapy.Field()
    coldDef = scrapy.Field()
    resistColdDef = scrapy.Field()
    resistColdDefLimit = scrapy.Field()
    fireAtt = scrapy.Field()
    fireDef = scrapy.Field()
    resistFireDef = scrapy.Field()
    resistFireDefLimit = scrapy.Field()
    lightAtt = scrapy.Field()
    lightDef = scrapy.Field()
    resistLightDef = scrapy.Field()
    resistLightDefLimit = scrapy.Field()
    postionAtt = scrapy.Field()
    postionDef = scrapy.Field()
    resistPostionDef = scrapy.Field()
    resistPostionDefLimit = scrapy.Field()
    chuanCiShangHai = scrapy.Field()
    chuanCiJianMian = scrapy.Field()


class equipWuHun(scrapy.Item):
    url = scrapy.Field()
    growRate = scrapy.Field()
    compandLevel = scrapy.Field()
    wuHunExtLanNum = scrapy.Field()
