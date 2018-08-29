# -*- coding: UTF-8 -*-
import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["changyou.com"]
    start_urls = [
        "http://tl.cyg.changyou.com/goods/public",
        "http://tl.cyg.changyou.com/goods/selling"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        print response.xpath('//title').extract()