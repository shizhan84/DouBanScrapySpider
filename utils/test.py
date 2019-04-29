# -*- coding:utf-8 -*-

'''
$ python run_spider SPIDER_NAME PROCESS_CNT
'''
import os

from scrapy import cmdline



cmdline.execute('scrapy crawl example2'.split())