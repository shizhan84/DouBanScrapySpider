# DouBanScrapySpider

*基于scrapy框架开发的简单爬虫入门学习例子，功能是抓取豆瓣上评分较高的书籍信息并保存，供日常买书参考

**可用test.py测试**

其中使用了随机user_agent和代理服务器middlewares
数据存储了使用的类JsonWriterPipeline*

# 该例子包含：
- 单机版本SingletionSpider
- 分布式版本DistributedSpider
  1. 先运行init_start_urls.py初始化数据
  2. 需要redis缓存服务支持
  3. 支持运行中服务重启等

