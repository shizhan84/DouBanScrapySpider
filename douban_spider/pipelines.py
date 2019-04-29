# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class DoubanSpiderPipeline(object):
    def process_item(self, item, spider):
        return item

import json
class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open(file='items.json', mode='a+', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.file.write(json.dumps(item,ensure_ascii=False)+',\n')
        self.file.flush()
        return item