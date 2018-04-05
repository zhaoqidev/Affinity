


# 跑项目的命令行  注意一定要把命令路径切换到爬虫目录下不然会报找不到 
scrapy runspider my_spider.py


# redis数据库的发布爬虫命令 各待命爬虫开始爬虫
lpush youyuan:start_urls http://www.youyuan.com/find/beijing/mm18-25/advance-0-0-0-0-0-0-0/p1/


#redis数据库

redis-server.exe开启服务

redis-cli redis客户端开启


#mongoDB
net start mongoDB  开启数据库

mongo shell 进入交互模式