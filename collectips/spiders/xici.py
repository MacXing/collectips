# -*- coding: utf-8 -*-
import scrapy
from collectips import items

class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xici.com']
    start_urls = ['http://www.xicidaili.com/nn/1']

    def start_requests(self):
        urls = [scrapy.Request('http://www.xicidaili.com/nn/%s'%i) for i in range(1,2769)]
        yield urls

    def parse(self, response):
        table = response.xpath('//*[@id="ip_list"]/tbody')

        trs = table[0].xpath('tr')
        items=[]
        for tr in trs[1:]:
            item = items.CollectipsItem()
            item['ip'] = response.xpath('/td[2]/text()').extract()
            item['port'] = response.xpath('/td[3]/text()').extract()
            item['address'] = response.xpath('/td[4]/a/text()').extract()
            item['position'] = response.xpath('/td[5]/text()').extract()
            item['type'] = response.xpath('/td[6]/text()').extract()
            item['valide_time'] = response.xpath('/td[10]/text()').extract()
            items.append(item)
        yield items
