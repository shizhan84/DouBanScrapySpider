# -*- coding: utf-8 -*-
import scrapy
import logging
import re
from scrapy import Request,signals
from scrapy_redis.spiders import RedisSpider


class Example2Spider(RedisSpider):
    name = "example2"
    redis_key = 'douban'

    allowed_domains = ["douban.com"]
    #start_urls = ['https://book.douban.com/tag/']

    def parse(self, response):
        print(response.url)
        #yield Request('https://book.douban.com/tag/通信',callback=self.parse_tag)
        tags = response.xpath('//tbody/tr/td/a/@href')
        for tag in tags:
            logging.info(tag)
            url = tag.extract()
            if url.startswith('/tag/'):
                yield Request(response.urljoin(tag.extract()),callback=self.parse_tag)

    def parse_tag(self,response):
        if response.status == 403:
            return

        #获取某个标签下的高评分图书
        infos = response.xpath('//ul[@class="subject-list"]/li/div[@class="info"]')
        for info in infos:
            try:
                title = info.xpath('./h2/a/@title').extract_first()
                href = info.xpath('./h2/a/@href').extract_first()
                rating = info.xpath('./div/span[@class="rating_nums"]/text()').extract_first()
                pl = info.xpath('./div/span[@class="pl"]/text()').extract_first()
                pl = re.findall('\d+',pl)[0]
                if float(rating) > 9 :#评分高于9
                    print('%s  %s        评分=%s       热度=%s'%(href,title,rating,pl))
                    item = {'title':title,'href':href,'rating':rating,'pl':pl}
                    yield item
            except Exception as e:
                logging.info(href)
                pass
        next = response.xpath('//span[@class="next"]/a/@href').extract_first()
        if next is not None:
            yield Request(response.urljoin(next), callback=self.parse_tag)

