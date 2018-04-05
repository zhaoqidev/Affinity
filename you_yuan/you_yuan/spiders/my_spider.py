# -*- coding: utf-8 -*-
import re
import time

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider

from you_yuan.items import YouYuanItem


class MySpiderSpider(RedisCrawlSpider):
    name = 'my'
    # allowed_domains = ['youyuan.com']
    # start_urls = ['http://youyuan.com/']
    redis_key = "you_yuan: start spider"  # 主redis发布的令牌

    def __init__(self, *args, **kwargs):
        """
        动态获取domain
        :param args:
        :param kwargs:
        """
        domain = kwargs.pop('domain', '')
        self.allow_domains = filter(None, domain.strip(','))
        super(MySpiderSpider, self).__init__(*args, **kwargs)

    page_links = LinkExtractor(allow=r"youyuan.com/find/beijing/mm18-26/advance-0-0-0-0-0-0-0/p\d+/")
    profile_links = LinkExtractor(allow=r"youyuan.com/\d+-profile/")

    rules = (
        Rule(page_links),
        Rule(profile_links, callback='parse_item'),
    )

    def parse_item(self, response):
        item = YouYuanItem()

        item['user_name'] = self.get_user_name()
        item['age'] = self.get_age()
        item['head_url'] = self.get_header_url()
        item['image_url'] = self.get_images_url()
        item['content'] = self.get_content()
        item['place_home'] = self.get_place_from()
        item['education'] = self.get_education()
        item['hobby'] = self.get_hobby()
        item['source'] = response.url
        yield item

    def get_user_name(self, response):
        username = response.xpath("//dl[@class='personal_cen']//div[@class='main']/strong/text()").extract()
        if len(username):
            username = username[0]
        else:
            username = "NULL"
        return username.strip()

    def get_age(self, response):
        age = response.xpath("//dl[@class='personal_cen']//dd/p/text()").extract()
        if len(age):
            age = re.findall(u"\d+岁", age[0])[0]
        else:
            age = "NULL"
        return age.strip()

    def get_header_url(self, response):
        header_url = response.xpath("//dl[@class='personal_cen']/dt/img/@src").extract()
        if len(header_url):
            header_url = header_url[0]
        else:
            header_url = "NULL"
        return header_url.strip()

    def get_images_url(self, response):
        images_url = response.xpath("//div[@class='ph_show']/ul/li/a/img/@src").extract()
        if len(images_url):
            images_url = ", ".join(images_url)
        else:
            images_url = "NULL"
        return images_url

    def get_content(self, response):
        content = response.xpath("//div[@class='pre_data']/ul/li/p/text()").extract()
        if len(content):
            content = content[0]
        else:
            content = "NULL"
        return content.strip()

    def get_place_from(self, response):
        place_from = response.xpath("//div[@class='pre_data']/ul/li[2]//ol[1]/li[1]/span/text()").extract()
        if len(place_from):
            place_from = place_from[0]
        else:
            place_from = "NULL"
        return place_from.strip()

    def get_education(self, response):
        education = response.xpath("//div[@class='pre_data']/ul/li[3]//ol[2]/li[2]/span/text()").extract()
        if len(education):
            education = education[0]
        else:
            education = "NULL"
        return education.strip()

    def get_hobby(self, response):
        hobby = response.xpath("//dl[@class='personal_cen']//ol/li/text()").extract()
        if len(hobby):
            hobby = ",".join(hobby).replace(" ", "")
        else:
            hobby = "NULL"
        return hobby.strip()
