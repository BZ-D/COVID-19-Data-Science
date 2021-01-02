# -!- coding: utf-8 -!-
from lxml import etree
# 无头浏览器 + 反检测selenium
from selenium import webdriver
from time import sleep
# 实现规避检测
from selenium.webdriver import ChromeOptions
import random
import re

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

# 实例化浏览器，传入参数
browser = webdriver.Chrome(
    executable_path=r'C:\Users\Ding\Desktop\Crawler-Studying\studyfiles\src\前期学习\chromedriver.exe', options=option)
browser.get('https://weibo.com/cctvxinwen?is_all=1&stat_date=202005&page=1')
sleep(20)
browser.get('https://weibo.com/cctvxinwen?is_all=1&stat_date=202005&page=1')
sleep(6)
html = browser.page_source
tree = etree.HTML(html)

# 对转发、评论、点赞数的获取
row_lines = tree.xpath('//ul[@class="WB_row_line WB_row_r4 clearfix S_line2"]')
for row_line in row_lines:
    zhuan_fa_li = row_line.xpath('./li[2]')
    zhuan_fa_number = zhuan_fa_li[0].xpath('./a/span/span/span//text()')[1]
    ping_lun_li = row_line.xpath('./li[3]')
    ping_lun_number = ping_lun_li[0].xpath('./a/span/span/span//text()')[1]
    zan_li = row_line.xpath('./li[4]')
    zan_number = zan_li[0].xpath('./a/span/span/span//text()')[1]
