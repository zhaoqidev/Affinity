# coding=utf-8
""" 
@author: stromqi
@file: process_item_for_mongo.py 
@email:245876200@qq.com
@time: 2018/04/05 
@github: github.com/stromqi
"""

import redis
import pymongo
import json
import scrapy.log

"""
redis mongo数据库
"""


def process_item():
    redis_client = redis.Redis(host="127.0.0.1", port=6379, db="0")
    mongo_client = pymongo.MongoClient(host="127.0.0.1", port=27017)
    db_name = mongo_client["youyuan"]
    sheet_name = db_name["beijing_area_mm"]

    while True:
        source, data = redis_client.blpop("yy:items")  # list[] or tuple()
        data = json.load(data)
        sheet_name.insert(data)
        scrapy.log.msg("log" + source)
        scrapy.log.msg("log" + data)


if __name__ == '__main__':
    process_item()
