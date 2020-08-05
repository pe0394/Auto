from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

dr = webdriver.Chrome('d:\chromedriver.exe')
dr.maximize_window()
dr.get('http://test.gq.eduzibo.com/')
waittime = 30
mintime = 5

dr.implicitly_wait(waittime)

#教师操作
#首页登录按钮
dr.find_element_by_css_selector('.glyphicon-log-in').click()

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
time.sleep(mintime)
dr.find_element_by_link_text('自主备课').click()
dr.implicitly_wait(waittime)
dr.find_element_by_link_text('集体备课').click()
dr.implicitly_wait(waittime)
dr.find_element_by_link_text('录播评课').click()
dr.implicitly_wait(waittime)
dr.find_element_by_link_text('一师一优课').click()
dr.implicitly_wait(waittime)
dr.find_element_by_link_text('在线课堂').click()
dr.implicitly_wait(waittime)
dr.find_element_by_link_text('名师课堂').click()
dr.implicitly_wait(waittime)
dr.find_element_by_link_text('主题研讨').click()
dr.implicitly_wait(waittime)
dr.find_element_by_link_text('问卷调查').click()
dr.implicitly_wait(waittime)
dr.find_element_by_link_text('投票活动').click()
dr.implicitly_wait(waittime)
dr.find_element_by_link_text('其他活动').click()
dr.implicitly_wait(waittime)
dr.find_element_by_link_text('教研组').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-教研-集体备课
jy = dr.find_element_by_xpath("//span[contains(.,'教研')]")
ActionChains(dr).move_to_element(jy).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'集体备课')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-教研-录播评课
jy = dr.find_element_by_xpath("//span[contains(.,'教研')]")
ActionChains(dr).move_to_element(jy).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'录播评课')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-教研-主题研讨
jy = dr.find_element_by_xpath("//span[contains(.,'教研')]")
ActionChains(dr).move_to_element(jy).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'主题研讨')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-教研-一师一优课
jy = dr.find_element_by_xpath("//span[contains(.,'教研')]")
ActionChains(dr).move_to_element(jy).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//div[5]/ul/li[5]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)

#导航空间点击
dr.find_element_by_xpath("//span[contains(.,'空间')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//a[contains(text(),'教师')]").click()
dr.implicitly_wait(waittime)
dr.find_element_by_xpath("//a[contains(text(),'学生')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-空间-个人空间
kj = dr.find_element_by_xpath("//span[contains(.,'空间')]")
ActionChains(dr).move_to_element(kj).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'个人空间')]").click()
time.sleep(mintime)
dr.find_element_by_id('tab-我的私信').click()
dr.implicitly_wait(waittime)
dr.find_element_by_id('tab-班级消息').click()
dr.implicitly_wait(waittime)
dr.find_element_by_id('tab-问答').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-空间-教育空间
kj = dr.find_element_by_xpath("//span[contains(.,'空间')]")
ActionChains(dr).move_to_element(kj).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'教育空间')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)


#导航社区点击
dr.find_element_by_xpath("//span[contains(.,'社区')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('最新').click()
dr.implicitly_wait(waittime)
dr.find_element_by_link_text('浏览量').click()
time.sleep(mintime)
dr.find_element_by_link_text('首页').click()#返回首页
dr.implicitly_wait(waittime)
#首页-社区-教育社区
sq = dr.find_element_by_xpath("//span[contains(.,'社区')]")
ActionChains(dr).move_to_element(sq).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'教育社区')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('首页').click()#返回首页
dr.implicitly_wait(waittime)



dr.close()