import requests
from lxml import etree

# 从https://www.aqistudy.cn/historydata/中解析出所有城市的名称

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

url = 'https://www.aqistudy.cn/historydata/'
response = requests.get(url=url,headers=headers)
page_text = response.text

hot_cities = []
all_cities = []
tree = etree.HTML(page_text)

hot_li_list = tree.xpath('//div[@class="hot"]/div[2]/ul/li')
all_li_list = tree.xpath('//div[@class="all"]/div[2]/ul/div[2]/li')

for hot_li in hot_li_list:
    hot_name = hot_li.xpath('./a/text()')[0]
    hot_cities.append(hot_name)
for li in all_li_list:
    name = li.xpath('./a/text()')[0]
    all_cities.append(name)
print('热门城市：')
for item in hot_cities:
    print(item)

print()
print('所有城市：')
for item in all_cities:
    print(item)