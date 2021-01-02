# -!- coding: utf-8 -!-
from lxml import etree
# 无头浏览器 + 反检测selenium
from selenium import webdriver
from time import sleep
# 实现规避检测
from selenium.webdriver import ChromeOptions
import random


def go():
    # 实现规避检测
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])

    # 实例化浏览器，传入参数
    browser = webdriver.Chrome(
        executable_path=r'C:\Users\Ding\Desktop\Crawler-Studying\studyfiles\src\前期学习\chromedriver.exe', options=option)

    # 请求
    # 二月：人民网，疫情从扩散到逐渐控制稳定
    # 三月：央视新闻，聚焦于逐渐复工复产，英雄凯旋，快递恢复等
    # 四月：人民日报，中国疫情得到全面稳定控制，各地防控有序进行，外国疫情逐渐爆发、严重
    browser.get('https://weibo.com/cctvxinwen?is_all=1&stat_date=202003&page=')
    sleep(30)  # 手动登录微博
    sumpage = 38
    count = 214
    fw = open(r'C:\Users\Ding\Desktop\Crawler-Studying\studyfiles\src\微博数据测试\微博数据\3月微博数据.txt', "a", encoding='utf-8')


    for page in range(6, sumpage + 1):
        browser.get('https://weibo.com/cctvxinwen?is_all=1&stat_date=202003&page=' + str(page))
        sleep(7)

        try:
            Infos = getContent(browser)
        except IndexError:
            print('第' + str(page) + '页获取失败！正在尝试重新获取……')
            browser.get('https://weibo.com/cctvxinwen?is_all=1&stat_date=202003&page=' + str(page))
            sleep(9)
            try:
                Infos = getContent(browser)
            except IndexError:
                print('重新获取失败！')

        allComments = getComment(page, browser)

        validNum = min(len(Infos[0]), len(Infos[1]), len(Infos[2]), len(allComments))


        for i in range(0, validNum):
            fw.write('第' + str(count) + '条微博：\n')
            count += 1
            fw.write('微博内容：' + Infos[0][i] + '\n')
            fw.write('时间：' + Infos[2][i] + '\n')
            fw.write('转发数：' + Infos[1][i][0] + '\n')
            fw.write('评论数：' + Infos[1][i][1] + '\n')
            fw.write('点赞数：' + Infos[1][i][2] + '\n')
            fw.write('评论内容：\n')

            numOfComments = len(allComments[i])
            for j in range(0, numOfComments):
                fw.write(str(j + 1) + allComments[i][j] + '\n')

            fw.write('----------------------------------------------------------\n')
        print('第' + str(page) + '页写入成功。')
        sleep(10 + random.randint(1, 5))  # 设个随机的时间，不能爬太快

    fw.close()


def getContent(browser):
    # 先scroll三次到最底部，每次scroll后等待4秒，加载全部45条微博内容
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    sleep(12)
    commentBtn = browser.find_elements_by_xpath('//ul[@class="WB_row_line WB_row_r4 clearfix S_line2"]/li[3]/a')
    # 找到中间一个评论展开按钮，按一下，更新页面信息
    centralCommentBtn = commentBtn[15]
    centralCommentBtn.click()
    sleep(5)
    centralCommentBtn.click()
    sleep(5)

    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    sleep(7)
    # 向下滚动加载后15条
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    sleep(2)

    commentBtn = browser.find_elements_by_xpath('//ul[@class="WB_row_line WB_row_r4 clearfix S_line2"]/li[3]/a')
    # 找到最后一个评论展开按钮，按一下，更新页面信息，这时返回的page_source才是完整的，否则只会显示前15条
    finalCommentBtn = commentBtn[-1]
    finalCommentBtn.click()
    sleep(5)
    finalCommentBtn.click()
    sleep(5)
    html = browser.page_source

    tree = etree.HTML(html)
    # 用于存放45条（左右）的微博正文
    realContents = []
    # 用于存放每条对应的转发、评论、点赞数
    otherInfos = []

    # 对正文内容的提取
    wb_text_list = tree.xpath('//div[@class="WB_text W_f14"]')

    for div in wb_text_list:
        content = div.xpath('.//text()')
        Content = ''
        length = len(content)
        for i in range(0, length):
            Content = Content + content[i]
            # 拼接content
        # 消去换行符等冗余符号，得到微博内容
        realContent = "".join(Content.split())
        realContents.append(realContent)

    # 对微博时间的提取
    details = tree.xpath('//div[@class="WB_detail"]')
    times = []
    for detail in details:
        time = detail.xpath('./div[@class="WB_from S_txt2"]//text()')[1]
        times.append(time)

    # 对转发、评论、点赞数的获取
    row_lines = tree.xpath('//ul[@class="WB_row_line WB_row_r4 clearfix S_line2"]')
    for row_line in row_lines:
        zhuan_fa_li = row_line.xpath('./li[2]')
        zhuan_fa_number = zhuan_fa_li[0].xpath('./a/span/span/span//text()')[1]
        ping_lun_li = row_line.xpath('./li[3]')
        ping_lun_number = ping_lun_li[0].xpath('./a/span/span/span//text()')[1]
        zan_li = row_line.xpath('./li[4]')
        zan_number = zan_li[0].xpath('./a/span/span/span//text()')[1]
        otherInfo = [zhuan_fa_number, ping_lun_number, zan_number]
        otherInfos.append(otherInfo)

    return [realContents, otherInfos, times]

def getComment(page, browser):
    # 首先再请求一次网页
    browser.get('https://weibo.com/cctvxinwen?is_all=1&stat_date=202003&page=' + str(page))
    sleep(8)
    # 先scroll三次到最底部，每次scroll后等待7秒，加载全部45条微博内容
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    sleep(7)
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    sleep(7)
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    sleep(2)

    commentBtn = browser.find_elements_by_xpath('//ul[@class="WB_row_line WB_row_r4 clearfix S_line2"]/li[3]/a')
    # 找到所有展开评论的按钮，并依次点击之，注意点击后获取的browser.page_source只有评论相关的内容，并不包含正文，所以要单独存储
    # 再scroll回顶部
    browser.execute_script('window.scrollTo(0,0)')
    sleep(1)
    for btn in commentBtn:
        btn.click()
        sleep(3.5)

    html = browser.page_source
    tree = etree.HTML(html)
    ul_list = tree.xpath('//div[@node-type="feed_list_commentList"]')
    allComments = []

    for ul in ul_list:
        comments = []
        divs = ul.xpath('./div')
        for div in divs:
            comment = div.xpath('./div[2]/div[@class="WB_text"]//text()')[2]
            comments.append(comment)
        allComments.append(comments)

    return allComments



if __name__ == '__main__':
    go()
    print('HTML源码获取结束。')