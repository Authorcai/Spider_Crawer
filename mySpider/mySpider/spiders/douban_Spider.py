# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import MyspiderItem

class DoubanSpiderSpider(scrapy.Spider):
    # 爬虫名称
    name = 'douban_Spider'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 使用的入 口url
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
    # print(response.text)
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for i_item in movie_list:
            douban_item = MyspiderItem()
            # 获取电影序号
            douban_item['serial_number'] = i_item.xpath(".//div[@class='item']//em/text()").extract_first()
            # 获取电影名称
            douban_item['movie_name'] = i_item.xpath(".//div[@class='hd']/a/span/text()").extract_first()
            # 获取电影介绍
            content = i_item.xpath(".//div[@class='bd']//p[1]/text()").extract()
            for i_content in content:
                content_s = "".join(i_content.split())
                douban_item['introduction'] = content_s
            # 获取电影简介
            douban_item['evaluate'] = i_item.xpath(".//div[@class='star']//span[4]/text()").extract_first()
            # 获取电影的评分
            douban_item['stars'] = i_item.xpath(".//div[@class='star']/span[2]/text()").extract_first()
            # 获取电影的评价
            douban_item['describe'] = i_item.xpath(".//p[@class='quote']/span/text()").extract_first()
            yield douban_item
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request('http://movie.douban.com/top250'+next_link,callback=self.parse)