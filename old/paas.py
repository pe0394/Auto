from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

dr = webdriver.Chrome('d:\chromedriver.exe')
dr.maximize_window()
time.sleep(1)

dr.get('http:\\paas.forclass.net')

dr.implicitly_wait(5)

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
#作业系统
dr.find_element_by_link_text('作业系统').click()

time.sleep(10)

#遮罩点击
act = ActionChains(dr)
act.move_by_offset(200, 100).click().perform()
time.sleep(5)

dr.find_element_by_id('kemu').click()
time.sleep(5)

#选择学段，小学语文三年级上
dr.find_element_by_css_selector("div[title='小学']").click()
time.sleep(5)
dr.find_element_by_css_selector("div[title='语文']").click()
time.sleep(5)
dr.find_element_by_css_selector("div[title='人教版']").click()
time.sleep(5)
dr.find_element_by_css_selector("div[title='三年级上']").click()
time.sleep(5)
dr.find_element_by_css_selector('.el-filter-btn').click() #确定



#布置作业试卷，我的创建
dr.find_element_by_css_selector("div[title='我的创建']").click()
time.sleep(5)

dr.find_element_by_css_selector('.paper-item:nth-child(1) .paper-edit')

zuoye = dr.find_element_by_css_selector('.paper-item:nth-child(1) .paper-edit')

act.move_to_element(zuoye).perform()
time.sleep(5)

dr.find_element_by_css_selector('.paper-edit:nth-child(3)').click()
time.sleep(5)

dr.find_element_by_css_selector('.ass-dlg-btnnext').click()
time.sleep(5)

dr.find_element_by_css_selector('.ass-dlg-clxtabs .ass-class-check').click()
time.sleep(5)

dr.find_element_by_css_selector('.ass-dlg-wbtn').click()#确定按钮
time.sleep(5)

#账号退出
dr.find_element_by_css_selector('.menulist').click()
time.sleep(5)
dr.find_element_by_id('logout').click()
time.sleep(5)

#学生操作
#首页登录按钮
dr.find_element_by_css_selector('.glyphicon-login').click()
time.sleep(5)
#输入账号
login = dr.find_element_by_id('login-name')
login.send_keys('sqa01s10')
#输入密码
pwd = dr.find_element_by_id('login-pwd')
pwd.send_keys('666666')
#登录按钮
dr.find_element_by_css_selector('.btnlogin').click()
time.sleep(5)
#作业系统
dr.find_element_by_link_text('作业系统').click()
time.sleep(5)
#作答
act = ActionChains(dr)
act.move_to_element(dr.find_element_by_css_selector('tr:nth-child(1) .icon-write')).perform()
time.sleep(5)
dr.find_element_by_css_selector('.icon-write:nth-child(2)').click()
time.sleep(5)
#手写答题
dr.find_element_by_css_selector('.question_body:nth-child(3) > .ques_funcs_img_item').click()
time.sleep(5)

dr.find_element_by_id('cnvs_temp').click()

huabu = dr.find_element_by_id('cnvs_temp')
act = ActionChains(dr)
act.move_to_element(huabu).click_and_hold().perform()
act.move_to_element(huabu).perform()
act.move_by_offset(200, 100).click().perform()
act.move_to_element(huabu).release().perform()
dr.find_element_by_id('cnvs_temp').click()
dr.find_element_by_css_selector('.cnvs_opt_ok').click()


#横线作答
dr.find_element_by_css_selector('span:nth-child(3) > .qoption > textarea').send_keys('担心')

dr.find_element_by_css_selector('.qoption:nth-child(2) > textarea').send_keys('扁担')
#图片上传
dr.find_element_by_css_selector('#q256853 .ques_funcs_img').click()

upload = dr.find_element_by_id('q_file256853')
time.sleep(5)
upload.send_keys('D:\\test.jpg')

#手写作答二
dr.find_element_by_css_selector('#q256857 .ques_funcs_img_item').click()
time.sleep(5)

dr.find_element_by_id('cnvs_temp').click()
huabu = dr.find_element_by_id('cnvs_temp')
act = ActionChains(dr)
act.move_to_element(huabu).click_and_hold().perform()
act.move_to_element(huabu).perform()
act.move_by_offset(200, 100).click().perform()
act.move_to_element(huabu).release().perform()
dr.find_element_by_id('cnvs_temp').click()
dr.find_element_by_css_selector('.cnvs_opt_ok').click()
time.sleep(10)
dr.find_element_by_css_selector('.el-dati-btn-submit > span').click()

dr.find_element_by_css_selector('.dlg-btn-submit').click()

dr.quit()
