from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

dr = webdriver.Chrome('d:\chromedriver.exe')
dr.maximize_window()

dr.get('http:\\paas.forclass.net')
waittime = 10
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
pwd.send_keys('654321')
#登录按钮
dr.find_element_by_css_selector('.btnlogin').click()
time.sleep(5)

#作业系统
dr.find_element_by_link_text('作业系统').click()
time.sleep(5)

#遮罩点击
act = ActionChains(dr)
act.move_by_offset(200, 100).click().perform()
time.sleep(waittime)

dr.find_element_by_id('kemu').click()
time.sleep(waittime)

#选择学段，小学语文三年级上
dr.find_element_by_css_selector("div[title='小学']").click()
time.sleep(waittime)
dr.find_element_by_css_selector("div[title='语文']").click()
time.sleep(waittime)
dr.find_element_by_css_selector("div[title='人教版']").click()
time.sleep(waittime)
dr.find_element_by_css_selector("div[title='三年级上']").click()
time.sleep(waittime)
dr.find_element_by_css_selector('.el-filter-btn').click() #确定



#布置作业试卷，我的创建
dr.find_element_by_css_selector("div[title='我的创建']").click()
time.sleep(waittime)

dr.find_element_by_css_selector('.paper-item:nth-child(1) .paper-edit')

zuoye = dr.find_element_by_css_selector('.paper-item:nth-child(1) .paper-edit')

act.move_to_element(zuoye).perform()
time.sleep(waittime)

dr.find_element_by_css_selector('.paper-edit:nth-child(3)').click()
time.sleep(waittime)

dr.find_element_by_css_selector('.ass-dlg-btnnext').click()
time.sleep(waittime)

dr.find_element_by_css_selector('.ass-dlg-clxtabs .ass-class-check').click()
time.sleep(waittime)

dr.find_element_by_css_selector('.ass-dlg-wbtn').click()#确定按钮
time.sleep(waittime)

#账号退出
dr.find_element_by_css_selector('.menulist').click()
time.sleep(waittime)
dr.find_element_by_id('logout').click()
dr.implicitly_wait(waittime)

dr.close()

