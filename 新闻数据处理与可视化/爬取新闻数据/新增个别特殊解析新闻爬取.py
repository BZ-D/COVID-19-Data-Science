import requests
from lxml import etree
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
    }
    url = 'http://xj.people.com.cn/n2/2020/0503/c394722-33993046.html'
    response= requests.get(url=url, headers=headers)
    response.encoding='GBK'
    page_text=response.text

    tree = etree.HTML(page_text)
    fp = open('人民日报五月份.txt', 'a', encoding='utf-8')

    li_listshijian = tree.xpath('//div[@class="clearfix w1000_320 text_title"]/div[@class="box01"]/div[@class="fl"]')
    fp.write('1、时间:'+li_listshijian[0].xpath('./text()')[0]+'\n')

    t_list = tree.xpath('//div[@class="clearfix w1000_320 text_title"]/h1')
    fp.write('标题:' +t_list[0].xpath('./text()')[0] + '\n')

    p_listxinwen = tree.xpath('//div[@class="clearfix w1000_320 text_con"]/div[@class="fl text_con_left"]/div[@class="box_con"]/p')
    for p in p_listxinwen:
        text=p.xpath('./text()')[0]
        fp.write(text)
    fp.write('\n')
