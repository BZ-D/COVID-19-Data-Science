# -!- coding: utf-8 -!-
from lxml import etree
# 无头浏览器 + 反检测selenium
from selenium import webdriver
from time import sleep
# 实现规避检测
from selenium.webdriver import ChromeOptions
import random

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

# 实例化浏览器，传入参数
browser = webdriver.Chrome(
    executable_path=r'C:\Users\Ding\Desktop\Crawler-Studying\studyfiles\src\前期学习\chromedriver.exe', options=option)

browser.get('https://weibo.com/cctvxinwen?is_all=1&stat_date=202003&page=1')
sleep(20)
browser.get('https://weibo.com/cctvxinwen?is_all=1&stat_date=202003&page=1')
sleep(3)

html = browser.page_source
tree = etree.HTML(html)

details = tree.xpath('//div[@class="WB_detail"]')

for detail in details:
    time = detail.xpath('./div[@class="WB_from S_txt2"]//text()')
