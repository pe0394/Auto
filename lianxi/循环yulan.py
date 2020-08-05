from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

dr = webdriver.Chrome('d:\chromedriver.exe')
dr.maximize_window()
dr.get('http:\\paas.forclass.net')
waittime = 30
mintime = 3

dr.implicitly_wait(waittime)

#教师操作
#首页登录按钮
dr.find_element_by_css_selector('.glyphicon-login').click()
#输入账号
login = dr.find_element_by_id('login-name')
login.send_keys('sqa001')
#输入密码
pwd = dr.find_element_by_id('login-pwd')
pwd.send_keys('666666')
#登录按钮
dr.find_element_by_css_selector('.btnlogin').click()
time.sleep(5)

def yulan():
    dr.find_element_by_link_text('同步资源').click()
    time.sleep(1)
    dr.find_element_by_xpath("//span[contains(.,'（人教新课标）一年级语文上册 哪座房子最漂亮.doc')]").click()
    time.sleep(1)
    dr.find_element_by_css_selector('.ivu-icon-close-round').click()
    time.sleep(1)

for _ in range(10):
    yulan()