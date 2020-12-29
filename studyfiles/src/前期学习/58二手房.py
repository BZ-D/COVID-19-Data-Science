# -*- coding:utf-8 -*-
import requests
from lxml import etree

if __name__ == "__main__":
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    url = 'https://nj.58.com/ershoufang/'
    #获取url源码数据
    page_text = requests.get(url=url, headers = headers).text
    #数据解析
    tree= etree.HTML(page_text)
    #找到二手房标题信息，先获取所有相关的li标签
    li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')

    fp = open('58.txt', 'w', encoding='utf-8')
    #逐个解析li标签内容
    for li in li_list:
        title = li.xpath('./div[2]/h2/a/text()')[0]
        print(title)
        fp.write(title+'\n')