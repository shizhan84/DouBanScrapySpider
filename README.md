# DouBanScrapySpider

> 一个基于scrapy框架开发的简单爬虫入门学习例子，目的是抓取保存豆瓣上评分较高的书籍信息。
其中使用了随机user_agent和代理服务middlewares
数据存储了使用的类JsonWriterPipeline

**可用test.py测试**

# 该例子包含：
- 单机版本SingletionSpider
- 分布式版本DistributedSpider
  1. 先运行init_start_urls.py初始化数据
  2. 需要redis缓存服务支持
  3. 支持运行中服务重启等

