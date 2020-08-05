from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest
dr = webdriver.Chrome('d:\chromedriver.exe')
dr.maximize_window()
dr.get('http://test.zy.bnuedu.com/')
waittime = 30
mintime = 5

dr.implicitly_wait(waittime)

#教师操作
#首页登录按钮
dr.find_element_by_css_selector('.glyphicon-login').click()

#输入账号
login = dr.find_element_by_id('login-name')
login.send_keys('sqa006')
#输入密码
pwd = dr.find_element_by_id('login-pwd')
pwd.send_keys('123566')
#登录按钮
dr.find_element_by_css_selector('.btnlogin').click()
time.sleep(5)

#导航教研点击

dr.find_element_by_xpath("//span[contains(.,'教研')]").click()
#断言当前地址
a = dr.current_url
b = 'http://test.cm.bnuedu.com/Cm/Research'
if (a == b):
    print(u'教研地址，OK')
else:
    print('error')

time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页

dr.implicitly_wait(waittime)

#首页-教研-京师名师
jy = dr.find_element_by_xpath("//span[contains(.,'教研')]")
ActionChains(dr).move_to_element(jy).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'京师名师')]").click()
a = dr.current_url
b = 'http://test.zy.bnuedu.com/Ms'
if (a == b):
    print(u'京师名师地址，OK')
else:
    print(u'京师名师地址，error')


time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)

#首页-教研-京师教研

jy = dr.find_element_by_xpath("//span[contains(.,'教研')]")
ActionChains(dr).move_to_element(jy).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'京师教研')]").click()
time.sleep(mintime)
a = dr.current_url
b = 'http://test.cm.bnuedu.com/Cm/Research'
if (a == b):
    print(u'京师教研地址，OK')
else:
    print(u'京师教研地址，error')
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)


#导航空间点击
dr.find_element_by_xpath("//span[contains(.,'空间')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//a[contains(text(),'教师')]").click()
dr.implicitly_wait(waittime)
dr.find_element_by_xpath("//a[contains(text(),'学生')]").click()
time.sleep(mintime)
a = dr.current_url
b = 'http://test.zy.bnuedu.com/Zone/Edu/Student'
if (a == b):
    print(u'空间地址，OK')
else:
    print(u'空间地址，error')
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-空间-京师空间
kj = dr.find_element_by_xpath("//span[contains(.,'空间')]")
ActionChains(dr).move_to_element(kj).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'京师空间')]").click()
a = dr.current_url
b = 'http://test.zy.bnuedu.com/Zone/Edu/School'
if (a == b):
    print(u'京师空间地址，OK')
else:
    print(u'京师空间地址，error')
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页



dr.close()