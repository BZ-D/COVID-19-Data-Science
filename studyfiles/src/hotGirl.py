import requests
from lxml import etree
import os
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}

url = 'http://pic.netbian.com/4kmeinv/'
# 获取url源码数据
response = requests.get(url=url, headers=headers)
page_text = response.text
response.close()
time.sleep(3)

# 数据解析
tree = etree.HTML(page_text)
# 找到二手房标题信息，先获取所有相关的li标签
li_list = tree.xpath('//div[@class="slist"]/ul/li')

if not os.path.exists('./picLibs'):
    os.mkdir('./picLibs')

for li in li_list:
    img_src = 'http://pic.netbian.com/' + li.xpath('./a/img/@src')[0]
    img_name = (li.xpath('./a/img/@alt')[0] + '.jpg').encode('iso-8859-1').decode('gbk')
    print(img_name)
    print(img_src)

    response = requests.get(url=img_src, headers=headers)
    img_data = response.content
    response.close()
    time.sleep(3)

    img_path = 'picLibs/' + img_name

    with open(img_path, 'wb') as fp:
        fp.write(img_data)
        print(img_name + '下载完成。')
