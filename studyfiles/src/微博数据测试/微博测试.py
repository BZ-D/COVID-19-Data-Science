from lxml import etree
# 无头浏览器 + 反检测selenium
from selenium import webdriver
from time import sleep
# 实现规避检测
from selenium.webdriver import ChromeOptions
import random

# 实现规避检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

# 实例化浏览器，传入参数
browser = webdriver.Chrome(
    executable_path=r'C:\Users\Ding\Desktop\Crawler-Studying\studyfiles\src\前期学习\chromedriver.exe', options=option)

# 测试
browser.get('https://weibo.com/renminwang?is_all=1&stat_date=202002&page=')
sleep(30)  # 手动登录微博
sumpage = 65 # 2月份共65页
itemsPerPage = 45 # 每页45条微博

for page in range(1, sumpage + 1):
    browser.get('https://weibo.com/renminwang?is_all=1&stat_date=202002&page=' + str(page))
    # 先scroll三次到最底部，每次scroll后等待4秒，加载全部45条微博内容
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    sleep(4)
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    sleep(4)
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    sleep(4)
    # 再scroll回顶部
    browser.execute_script('window.scrollTo(0,0)')
    sleep(1)

    # 存放已经展开了所有评论的网页解析后源码，只包括正文
    html = browser.page_source
    contentStr = '第' + str(page) + '页微博正文主页面.txt'
    content = open(contentStr, 'a', encoding='utf-8')
    content.write(html + '\n')
    content.close()

    # 找到所有展开评论的按钮，并点击之，注意点击后获取的browser.page_source只有评论相关的内容，并不包含正文，所以要单独存储
    commentBtn = browser.find_elements_by_xpath('//ul[@class="WB_row_line WB_row_r4 clearfix S_line2"]/li[3]/a')
    for btn in commentBtn:
        btn.click()
        sleep(2.5)

    # 创建文件
    commentStr = '第' + str(page) + '页微博评论.txt'
    comment = open(commentStr, 'a', encoding='utf-8')
    comment.write(html + '\n')
    print(commentStr + '写入成功。')

    sleep(10 + random.randint(1, 9))  # 设个随机的时间，不能爬太快
    comment.close()

print('HTML源码获取结束。')
