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
    browser.get('https://weibo.com/rmrb?is_all=1&stat_date=202004&page=')
    sleep(30)  # 手动登录微博
    sumpage = 38

    for page in range(29, sumpage + 1):
        browser.get('https://weibo.com/rmrb?is_all=1&stat_date=202004&page=' + str(page))
        sleep(7)

        try:
            getContent(page, browser)
        except IndexError as e:
            print('第' + str(page) + '页获取失败！')
            continue

        getComment(page, browser)
        print('第' + str(page) + '页写入成功。')
        sleep(10 + random.randint(1, 9))  # 设个随机的时间，不能爬太快


def getContent(page, browser):
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
    sleep(7)

    commentBtn = browser.find_elements_by_xpath('//ul[@class="WB_row_line WB_row_r4 clearfix S_line2"]/li[3]/a')
    # 找到最后一个评论展开按钮，按一下，更新页面信息，这时返回的page_source才是完整的，否则只会显示前15条
    finalCommentBtn = commentBtn[-1]
    finalCommentBtn.click()
    sleep(5)
    finalCommentBtn.click()
    sleep(5)
    html = browser.page_source

    contentStr = '第' + str(page) + '页微博正文主页面.txt'
    content = open('./四月份微博数据（人民日报）/' + contentStr, 'a', encoding='utf-8')
    content.write(html + '\n')
    content.close()

def getComment(page, browser):
    # 首先再请求一次网页
    browser.get('https://weibo.com/rmrb?is_all=1&stat_date=202004&page=' + str(page))
    sleep(8)
    # 先scroll三次到最底部，每次scroll后等待7秒，加载全部45条微博内容
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    sleep(7)
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    sleep(7)
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    sleep(7)

    commentBtn = browser.find_elements_by_xpath('//ul[@class="WB_row_line WB_row_r4 clearfix S_line2"]/li[3]/a')
    # 找到所有展开评论的按钮，并依次点击之，注意点击后获取的browser.page_source只有评论相关的内容，并不包含正文，所以要单独存储
    # 再scroll回顶部
    browser.execute_script('window.scrollTo(0,0)')
    sleep(1)
    for btn in commentBtn:
        btn.click()
        sleep(3.5)

    html = browser.page_source
    # 创建文件
    commentStr = '第' + str(page) + '页微博评论.txt'
    comment = open('./四月份微博数据（人民日报）/' + commentStr, 'a', encoding='utf-8')
    comment.write(html + '\n')
    comment.close()


if __name__ == '__main__':
    go()
    print('HTML源码获取结束。')