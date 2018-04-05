# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YouYuanItem(scrapy.Item):
    user_name = scrapy.Field()  # 用户名
    age = scrapy.Field()  # 年龄
    head_url = scrapy.Field()  # 头像ur
    image_url = scrapy.Field()  # 相册
    content = scrapy.Field()  # 简介
    place_home = scrapy.Field()  # 籍贯
    education = scrapy.Field()  # 教育
    hobby = scrapy.Field()  # 爱好
    source = scrapy.Field()  # 主页地址
    time = scrapy.Field()  # utc 时间
    spider = scrapy.Field()  # 爬虫时间
