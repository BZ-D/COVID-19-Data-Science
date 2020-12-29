from selenium import webdriver
from lxml import etree
from time import sleep

bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('https://qzone.qq.com/')
page_text = bro.page_source
tree = etree.HTML(page_text)
bro.switch_to.frame('login_frame')
# 切换到账号密码登录
switch_to_login = bro.find_element_by_id('switcher_plogin')
switch_to_login.click()
sleep(1)
# 定位账号框、密码框
userName = bro.find_element_by_id('u')
sleep(1)
passwd = bro.find_element_by_id('p')
sleep(1)
# 输入账号密码
userName.send_keys('123')
sleep(1)
passwd.send_keys('123')
sleep(1)
# 定位并点击登录按钮
loginBtn = bro.find_element_by_id('login_button')
loginBtn.click()
sleep(2)
bro.quit()
