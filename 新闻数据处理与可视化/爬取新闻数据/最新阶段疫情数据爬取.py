import requests
from lxml import etree
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
    }
    url="https://so.jstv.com/?keyword=%E7%96%AB%E6%83%85&page="
    for i in range(120,239):
        urldetail=url+str(i)
        response = requests.get(url=urldetail, headers=headers)
        response.encoding = 'GBK'
        page_text = response.text
        tree = etree.HTML(page_text)
        li_list = tree.xpath('//div[@id="lzxw_warp"]/div[@class="lzxw_l"]/div[@class="lzxw_lxz"]/ul/li')
        for li in li_list:
            urlnei=li.xpath('./span/a/@href')[0]
            time=li.xpath('./div[@class="lzxw_per_r"]/p[@class="search_time"]/text()')[0]
            responsedetail = requests.get(url=urlnei, headers=headers)
            responsedetail.content.decode('gb18030','ignore')
            page_textdetail = responsedetail.content
            treedetail = etree.HTML(page_textdetail)
            list=treedetail.xpath('//div[0]/p/text()')
            fp = open('最新一轮疫情.txt', 'a', encoding='utf-8')
            li_listshijian = treedetail.xpath(
                '//div[@class="bd clearfix"]/div[@class="main fL"]/div[@class="article"]/div[@class="assist"]/p[@class="info fL"]/span[@class="time"]')
            if treedetail.xpath('//div[0]/p/text()') != ["对不起，此页面不存在"]:
                if li_listshijian != []:
                    fp.write('*、时间:' + li_listshijian[0].xpath('./text()')[0] + '\n')

                    t_list = treedetail.xpath(
                        '//div[@class="bd clearfix"]/div[@class="main fL"]/div[@class="article"]/h3')
                    fp.write('标题:' + t_list[0].xpath('./text()')[0] + '\n')
                    p_listxinwen = treedetail.xpath(
                        '//div[@class="bd clearfix"]/div[@class="main fL"]/div[@class="article"]/div[@class="content"]/p')
                    for p in p_listxinwen:
                        if (p.xpath('./@style') != ["text-align:center;"]) & (p.xpath('./text()') != []):
                            text = p.xpath('./text()')[0]
                            fp.write(text)
                    fp.write('\n')
