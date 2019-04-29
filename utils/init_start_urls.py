#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis

# 将start_url 存储到redis中的redis_key中，让爬虫去爬取
redis_key = 'douban'

rediscli = redis.Redis(host='10.100.5.163', port=6379,password='123456', db=11, decode_responses=True)

flushdbRes = rediscli.flushdb()


rediscli.lpush(redis_key, "https://book.douban.com/tag/")


