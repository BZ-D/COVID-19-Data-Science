
from bs4 import BeautifulSoup
import re
from urllib import request
import urllib
import time
import xlwt
import selenium


def main():
    baseurl = "https://weibo.com/rmrb?is_all=1&stat_date=202002&page=10#feedtop"
    datalist = getData(baseurl)
    #savepath = r"C:\Users\Ding\Desktop\数据测试\人民日报测试.xls"

    #saveData(savepath, datalist)
    #print('爬取完成。')


# 提取的正则式
findLink = re.compile(r'<a href="(.*?)">')
findPicSrc = re.compile(r'src="(.*?)" width=')
findTitle = re.compile(r'<span class="title">(.*?)</span>')
findRate = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 从已获取的页面信息中解析数据
def getData(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl
        html = askURL(url)  # 保存获取到的网页源码
        print(html)
        break

        # 逐一解析数据
        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.find_all('div', class_='item'):
            data = []  # 保存每部电影的信息
            item = str(item)  # 转化成字符串，便于正则提取

            # 找电影名字
            titles = re.findall(findTitle, item)
            if (len(titles) == 2):
                ch_name = titles[0]
                ot_name = titles[1][3:]
                data.append(ch_name)
                data.append(ot_name)
            if (len(titles) == 1):
                ch_name = titles[0]
                data.append(ch_name)
                data.append(" ")  # 没有外文名也要添加一个空格串，以免后续信息窜位

            # 找电影链接
            link = re.findall(findLink, item)[0]
            data.append(link)

            # 找电影海报图片链接
            picSrc = re.findall(findPicSrc, item)[0]
            data.append(picSrc)

            # 找电影评价率
            rate = re.findall(findRate, item)[0]
            data.append(rate)

            # 找电影短评
            inq = re.findall(findInq, item)
            if (len(inq) == 1):
                data.append(inq[0])
            else:
                data.append(' ')

            # 找信息概述
            bd = re.findall(findBd, item)[0]
            data.append(bd)

            # 把data添加到datalist中
            datalist.append(data)

    return datalist


# 获取页面信息函数
def askURL(url):
    header = {
        "Cookie" : "SINAGLOBAL=4479130396921.655.1607081010156; login_sid_t=14f59ca30b069dc7dc6b2f84762acb9d; cross_origin_proto=SSL; _s_tentry=www.baidu.com; Apache=5768985895166.771.1608967431186; wb_view_log=1549*8721.2395833730697632; ULV=1608967431201:3:3:1:5768985895166.771.1608967431186:1607690671422; ALF=1640503446; wvr=6; wb_view_log_7315719825=1549*8721.2395833730697632; SSOLoginState=1608977348; SUB=_2A25y43uUDeRhGeFN6lcW8SfEyTmIHXVuLAXcrDV8PUJbkNANLRn-kW1NQHHaz4-9C_7QWBWTuhLIK_JnFibstS4h; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W54WqWpl7Q3EsqSOoiA7wRY5NHD95QNe02fS0241hzfWs4DqcjZxgxLdJfydo2Ee7tt; UOR=,,weibo.cn; webim_unReadCount=%7B%22time%22%3A1608983047921%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A1%2C%22msgbox%22%3A0%7D",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    req = request.Request(url, headers=header)
    html = ''

    try:
        response = request.urlopen(req)
        html = response.read().decode('utf-8')

    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)

    return html


# 保存数据
def saveData(savepath, datalist):
    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
    worksheet = workbook.add_sheet('Douban250')
    items = ('序号', '中文名', '外文名', '电影链接', '海报链接', '评价人数', '电影短评', '电影信息')
    for i in range(0, 8):
        worksheet.write(0, i, items[i])

    length = len(datalist)
    count = 1
    for i in range(1, length + 1):
        data = datalist[i - 1]
        print('正在写入第%d个电影的信息' % i)
        worksheet.write(i, 0, count)
        count += 1
        for j in range(0, 7):
            worksheet.write(i, j + 1, data[j])

    workbook.save(savepath)


if __name__ == "__main__":
    main()
