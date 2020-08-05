from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

dr = webdriver.Chrome('d:\chromedriver.exe')
dr.maximize_window()

dr.get('http://271bay.com/')
waittime = 30
mintime = 3
dr.implicitly_wait(waittime)


#教师操作
#首页登录按钮
dr.find_element_by_css_selector('.glyphicon-login').click()
#输入账号
login = dr.find_element_by_id('login-name')
login.send_keys('271sqa666')
#输入密码
pwd = dr.find_element_by_id('login-pwd')
pwd.send_keys('123456')
#登录按钮
dr.find_element_by_css_selector('.btnlogin').click()
time.sleep(5)



#导航资源点击
dr.find_element_by_xpath("//span[contains(.,'资源')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-资源-国家课程
zy = dr.find_element_by_xpath("//span[contains(.,'资源')]")
ActionChains(dr).move_to_element(zy).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'国家课程')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('应用商店').click()
time.sleep(mintime)
dr.find_element_by_link_text('我的资源').click()
time.sleep(mintime)
dr.find_element_by_link_text('国家课程').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-资源-我的资源
zy = dr.find_element_by_xpath("//span[contains(.,'资源')]")
ActionChains(dr).move_to_element(zy).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'我的资源')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)


#导航教学点击
dr.find_element_by_xpath("//span[contains(.,'教学')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)

#首页-教学-智慧课堂
jx = dr.find_element_by_xpath("//span[contains(.,'教学')]")
ActionChains(dr).move_to_element(jx).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//div[3]/ul/li").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-教学-导学案
jx = dr.find_element_by_xpath("//span[contains(.,'教学')]")
ActionChains(dr).move_to_element(jx).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'导学案')]").click()
time.sleep(5)
#遮罩点击
act = ActionChains(dr)
act.move_by_offset(200, 100).click().perform()
time.sleep(mintime)

#批阅
dr.find_element_by_link_text('批阅').click()
dr.implicitly_wait(waittime)
#统计分析
dr.find_element_by_link_text('统计分析').click()
dr.implicitly_wait(waittime)
#我的题库
dr.find_element_by_link_text('我的题库').click()
dr.implicitly_wait(waittime)
#布置
dr.find_element_by_link_text('布置').click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/div/div/div/div/div").click()#返回首页
dr.implicitly_wait(waittime)
#首页-教学-试题
jx = dr.find_element_by_xpath("//span[contains(.,'教学')]")
ActionChains(dr).move_to_element(jx).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'试题')]").click()
time.sleep(5)
#遮罩点击
act = ActionChains(dr)
act.move_by_offset(200, 100).click().perform()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/div/div/div/div/div").click()#返回首页
dr.implicitly_wait(waittime)

#导航教研点击
dr.find_element_by_xpath("//span[contains(.,'教研')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('教研组').click()
dr.implicitly_wait(waittime)
dr.find_element_by_link_text('教研会商').click()
dr.implicitly_wait(waittime)
dr.find_element_by_link_text('首页').click()#返回首页
dr.implicitly_wait(waittime)
#首页-教研-教研会商
jy = dr.find_element_by_xpath("//span[contains(.,'教研')]")
ActionChains(dr).move_to_element(jy).perform()
time.sleep(5)
dr.find_element_by_xpath("//li[contains(.,'教研会商')]").click()
dr.implicitly_wait(waittime)
dr.find_element_by_link_text('主题研讨').click()
time.sleep(mintime)
dr.find_element_by_link_text('问卷调查').click()
time.sleep(mintime)
dr.find_element_by_link_text('投票活动').click()
time.sleep(mintime)
dr.find_element_by_link_text('其他活动').click()
time.sleep(mintime)
dr.find_element_by_link_text('教研会商').click()
time.sleep(mintime)
dr.find_element_by_link_text('首页').click()#返回首页
dr.implicitly_wait(waittime)


#导航空间点击
dr.find_element_by_xpath("//span[contains(.,'空间')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//a[contains(text(),'教师')]").click()
time.sleep(5)
dr.find_element_by_xpath("//a[contains(text(),'学生')]").click()
time.sleep(5)
dr.find_element_by_xpath("//a[contains(text(),'学校')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-空间-学校空间
kj = dr.find_element_by_xpath("//span[contains(.,'空间')]")
ActionChains(dr).move_to_element(kj).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'学校空间')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('校本资源').click()
time.sleep(mintime)
dr.find_element_by_link_text('学校简介').click()
time.sleep(mintime)
dr.find_element_by_link_text('名师风采').click()
time.sleep(mintime)
dr.find_element_by_link_text('学校教师').click()
time.sleep(mintime)
dr.find_element_by_link_text('班级空间').click()
time.sleep(mintime)
dr.find_element_by_link_text('主页').click()
time.sleep(mintime)
dr.find_element_by_css_selector('.instback').click()#返回首页
dr.implicitly_wait(waittime)
#首页-空间-班级空间
kj = dr.find_element_by_xpath("//span[contains(.,'空间')]")
ActionChains(dr).move_to_element(kj).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'班级空间')]").click()
time.sleep(mintime)
dr.find_element_by_css_selector('.instback').click()#返回首页
dr.implicitly_wait(waittime)
#首页-空间-个人空间
kj = dr.find_element_by_xpath("//span[contains(.,'空间')]")
ActionChains(dr).move_to_element(kj).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'个人空间')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('我的私信').click()
time.sleep(mintime)
dr.find_element_by_link_text('班级消息').click()
time.sleep(mintime)
dr.find_element_by_link_text('我的问答').click()
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


#首页-统计-课堂统计
tj = dr.find_element_by_xpath("//span[contains(.,'统计')]")
ActionChains(dr).move_to_element(tj).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'课堂统计')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('导学统计').click()
time.sleep(mintime)
dr.find_element_by_link_text('课堂统计').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-统计-学业统计
tj = dr.find_element_by_xpath("//span[contains(.,'统计')]")
ActionChains(dr).move_to_element(tj).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'学业数据')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)


#导航活动点击
dr.find_element_by_xpath("//span[contains(.,'活动')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('发现活动').click()
dr.implicitly_wait(waittime)
dr.find_element_by_link_text('班级活动').click()
dr.implicitly_wait(waittime)
dr.find_element_by_link_text('我的活动').click()
dr.implicitly_wait(waittime)
dr.find_element_by_link_text('活动首页').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)


#首页-菜单-系统消息
list = dr.find_element_by_css_selector('.glyphicon-list')
ActionChains(dr).move_to_element(list).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'系统消息')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/header/div/div/div/div").click()#返回首页
dr.implicitly_wait(waittime)
#首页-菜单-我的私信
list = dr.find_element_by_css_selector('.glyphicon-list')
ActionChains(dr).move_to_element(list).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'我的私信')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/header/div/div/div/div").click()#返回首页
dr.implicitly_wait(waittime)
#首页-菜单-班级消息
list = dr.find_element_by_css_selector('.glyphicon-list')
ActionChains(dr).move_to_element(list).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'班级消息')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/header/div/div/div/div").click()#返回首页
dr.implicitly_wait(waittime)
#首页-菜单-@提到我的
list = dr.find_element_by_css_selector('.glyphicon-list')
ActionChains(dr).move_to_element(list).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'@提到我的')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('我的圈子').click()
dr.implicitly_wait(waittime)
dr.find_element_by_link_text('提到我的').click()
dr.implicitly_wait(waittime)
dr.find_element_by_link_text('好友/关注/粉丝').click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/header/div/div/div/div").click()#返回首页
dr.implicitly_wait(waittime)
#首页-菜单-我的问答
list = dr.find_element_by_css_selector('.glyphicon-list')
ActionChains(dr).move_to_element(list).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'我的问答')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)

#导航用户名点击
dr.find_element_by_css_selector('.uname').click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/header/div/div/div/div").click()#返回首页
dr.implicitly_wait(waittime)

#首页中部导航-教研中心
dr.find_element_by_link_text('教研会商').click()
time.sleep(mintime)
dr.find_element_by_link_text('首页').click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('教研管理').click()
time.sleep(mintime)
#首页中部导航-教学中心
dr.find_element_by_link_text('智慧课堂').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('导学案').click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/div/div/div/div/div").click()#浏览器回首页
time.sleep(mintime)
#首页中部导航-社区中心
dr.find_element_by_link_text('学校空间').click()
time.sleep(mintime)
dr.find_element_by_css_selector('.instback').click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('班级空间').click()
time.sleep(mintime)
dr.find_element_by_css_selector('.instback').click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('个人空间').click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/header/div/div/div/div").click()#浏览器回首页
time.sleep(mintime)
#首页中部导航-资源中心
dr.find_element_by_link_text('国家课程').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('我的资源').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#浏览器回首页
time.sleep(mintime)
#首页中部导航-数据管理
dr.find_element_by_link_text('课堂数据').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('学业数据').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('行规数据').click()
time.sleep(mintime)
dr.find_element_by_link_text('教研数据').click()
time.sleep(mintime)

#首页-用户名-个人中心
uname = dr.find_element_by_css_selector('.uname')
ActionChains(dr).move_to_element(uname).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'个人中心')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/div/div/div/div/div").click()#返回首页
dr.implicitly_wait(waittime)
#首页-用户名-个人中心
uname = dr.find_element_by_css_selector('.uname')
ActionChains(dr).move_to_element(uname).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'退出')]").click()
dr.implicitly_wait(waittime)




#学生操作
#首页登录按钮
dr.find_element_by_css_selector('.glyphicon-login').click()
#输入账号
login = dr.find_element_by_id('login-name')
login.send_keys('271tyt10s01')
#输入密码
pwd = dr.find_element_by_id('login-pwd')
pwd.send_keys('ABCabc01')
#登录按钮
dr.find_element_by_css_selector('.btnlogin').click()
time.sleep(5)




#导航教学点击
dr.find_element_by_xpath("//span[contains(.,'教学')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)

#首页-教学-智慧课堂
jx = dr.find_element_by_xpath("//span[contains(.,'教学')]")
ActionChains(dr).move_to_element(jx).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//div[3]/ul/li").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-教学-导学案
jx = dr.find_element_by_xpath("//span[contains(.,'教学')]")
ActionChains(dr).move_to_element(jx).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'导学案')]").click()
time.sleep(5)
#遮罩点击
act = ActionChains(dr)
act.move_by_offset(200, 100).click().perform()
time.sleep(mintime)

#待完成
dr.find_element_by_xpath("//div[@id='main']/div[2]/div/div/div/div/div[2]").click()
time.sleep(mintime)
#待批阅
dr.find_element_by_xpath("//div[@id='main']/div[2]/div/div/div/div/div[3]").click()
time.sleep(mintime)
#未提交
dr.find_element_by_xpath("//div[@id='main']/div[2]/div/div/div/div/div[4]").click()
time.sleep(mintime)
#批阅完成
dr.find_element_by_xpath("//div[@id='main']/div[2]/div/div/div/div/div").click()
time.sleep(mintime)
dr.find_element_by_link_text('自主训练').click()
time.sleep(mintime)
dr.find_element_by_link_text('错题本').click()
time.sleep(mintime)
dr.find_element_by_link_text('好题本').click()
time.sleep(mintime)
dr.find_element_by_link_text('我的成长').click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/div/div/div/div/div").click()#返回首页
dr.implicitly_wait(waittime)
#首页-教学-试题
jx = dr.find_element_by_xpath("//span[contains(.,'教学')]")
ActionChains(dr).move_to_element(jx).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'试题')]").click()
time.sleep(5)
#遮罩点击
act = ActionChains(dr)
act.move_by_offset(200, 100).click().perform()
time.sleep(mintime)
#今日作业
dr.find_element_by_xpath("//div[@id='main']/div[2]/div/div/div/div/div").click()
time.sleep(mintime)
#本周作业
dr.find_element_by_xpath("//div[@id='main']/div[2]/div/div/div/div/div[2]").click()
time.sleep(mintime)
#本月作业
dr.find_element_by_xpath("//div[@id='main']/div[2]/div/div/div/div/div[3]").click()
time.sleep(mintime)
dr.back()#返回首页
dr.implicitly_wait(waittime)


#导航空间点击
dr.find_element_by_xpath("//span[contains(.,'空间')]").click()
time.sleep(mintime)
#首页-空间-学校空间
kj = dr.find_element_by_xpath("//span[contains(.,'空间')]")
ActionChains(dr).move_to_element(kj).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'学校空间')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('校本资源').click()
time.sleep(mintime)
dr.find_element_by_link_text('学校简介').click()
time.sleep(mintime)
dr.find_element_by_link_text('名师风采').click()
time.sleep(mintime)
dr.find_element_by_link_text('学校教师').click()
time.sleep(mintime)
dr.find_element_by_link_text('班级空间').click()
time.sleep(mintime)
dr.find_element_by_link_text('主页').click()
time.sleep(mintime)
dr.find_element_by_css_selector('.instback').click()#返回首页
dr.implicitly_wait(waittime)
#首页-空间-班级空间
kj = dr.find_element_by_xpath("//span[contains(.,'空间')]")
ActionChains(dr).move_to_element(kj).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'班级空间')]").click()
time.sleep(mintime)
dr.find_element_by_css_selector('.instback').click()#返回首页
dr.implicitly_wait(waittime)


#导航活动点击
dr.find_element_by_xpath("//span[contains(.,'活动')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('发现活动').click()
time.sleep(mintime)
dr.find_element_by_link_text('我的活动').click()
time.sleep(mintime)
dr.find_element_by_link_text('活动首页').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)


#首页-菜单-系统消息-不跳转
list = dr.find_element_by_css_selector('.glyphicon-list')
ActionChains(dr).move_to_element(list).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'系统消息')]").click()
time.sleep(mintime)
#首页-菜单-我的私信-不跳转
list = dr.find_element_by_css_selector('.glyphicon-list')
ActionChains(dr).move_to_element(list).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'我的私信')]").click()
time.sleep(mintime)
#首页-菜单-班级消息-不跳转
list = dr.find_element_by_css_selector('.glyphicon-list')
ActionChains(dr).move_to_element(list).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'班级消息')]").click()
time.sleep(mintime)
#首页-菜单-@提到我的
list = dr.find_element_by_css_selector('.glyphicon-list')
ActionChains(dr).move_to_element(list).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'@提到我的')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('我的圈子').click()
time.sleep(mintime)
dr.find_element_by_link_text('提到我的').click()
time.sleep(mintime)
dr.find_element_by_link_text('好友/关注/粉丝').click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/header/div/div/div/div").click()#返回首页
dr.implicitly_wait(waittime)
#首页-菜单-我的问答
list = dr.find_element_by_css_selector('.glyphicon-list')
ActionChains(dr).move_to_element(list).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'我的问答')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)

#导航用户名点击
dr.find_element_by_css_selector('.uname').click()
time.sleep(mintime)


#首页中部导航-教研中心
dr.find_element_by_link_text('教研会商').click()
time.sleep(mintime)
dr.find_element_by_link_text('教研管理').click()
time.sleep(mintime)
#首页中部导航-教学中心
dr.find_element_by_link_text('智慧课堂').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('导学案').click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/div/div/div/div/div").click()#浏览器回首页
time.sleep(mintime)
#首页中部导航-社区中心
dr.find_element_by_link_text('学校空间').click()
time.sleep(mintime)
dr.find_element_by_css_selector('.instback').click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('班级空间').click()
time.sleep(mintime)
dr.find_element_by_css_selector('.instback').click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('个人空间').click()
time.sleep(mintime)
#首页中部导航-资源中心
dr.find_element_by_link_text('国家课程').click()
time.sleep(mintime)
dr.find_element_by_link_text('我的资源').click()
time.sleep(mintime)
#首页中部导航-数据管理
dr.find_element_by_link_text('课堂数据').click()
time.sleep(mintime)
dr.find_element_by_link_text('学业数据').click()
time.sleep(mintime)
dr.find_element_by_link_text('行规数据').click()
time.sleep(mintime)
dr.find_element_by_link_text('教研数据').click()
time.sleep(mintime)


#首页-用户名-个人中心
uname = dr.find_element_by_css_selector('.uname')
ActionChains(dr).move_to_element(uname).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'个人中心')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/div/div/div/div/div").click()#返回首页
dr.implicitly_wait(waittime)
#首页-用户名-个人中心
uname = dr.find_element_by_css_selector('.uname')
ActionChains(dr).move_to_element(uname).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'退出')]").click()
dr.implicitly_wait(waittime)



#管理员操作
#首页登录按钮
dr.find_element_by_css_selector('.glyphicon-login').click()
#输入账号
login = dr.find_element_by_id('login-name')
login.send_keys('271tyadm01')
#输入密码
pwd = dr.find_element_by_id('login-pwd')
pwd.send_keys('123456')
#登录按钮
dr.find_element_by_css_selector('.btnlogin').click()
time.sleep(5)



#导航资源点击
dr.find_element_by_xpath("//span[contains(.,'资源')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-资源-国家课程
zy = dr.find_element_by_xpath("//span[contains(.,'资源')]")
ActionChains(dr).move_to_element(zy).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'国家课程')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('应用商店').click()
time.sleep(mintime)
dr.find_element_by_link_text('我的资源').click()
time.sleep(mintime)
dr.find_element_by_link_text('国家课程').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-资源-我的资源
zy = dr.find_element_by_xpath("//span[contains(.,'资源')]")
ActionChains(dr).move_to_element(zy).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'我的资源')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)


#导航教学点击
dr.find_element_by_xpath("//span[contains(.,'教学')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)

#首页-教学-智慧课堂
jx = dr.find_element_by_xpath("//span[contains(.,'教学')]")
ActionChains(dr).move_to_element(jx).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//div[3]/ul/li").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)


#导航教研点击
dr.find_element_by_xpath("//span[contains(.,'教研')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('教研组').click()
time.sleep(mintime)
dr.find_element_by_link_text('教研会商').click()
time.sleep(mintime)
dr.find_element_by_link_text('首页').click()#返回首页
dr.implicitly_wait(waittime)
#首页-教研-教研会商
jy = dr.find_element_by_xpath("//span[contains(.,'教研')]")
ActionChains(dr).move_to_element(jy).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'教研会商')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('教研组').click()
time.sleep(mintime)
dr.find_element_by_link_text('教研会商').click()
time.sleep(mintime)
dr.find_element_by_link_text('首页').click()#返回首页
dr.implicitly_wait(waittime)


#导航空间点击
dr.find_element_by_xpath("//span[contains(.,'空间')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//a[contains(text(),'教师')]").click()
time.sleep(5)
dr.find_element_by_xpath("//a[contains(text(),'学生')]").click()
time.sleep(5)
dr.find_element_by_xpath("//a[contains(text(),'学校')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-空间-学校空间
kj = dr.find_element_by_xpath("//span[contains(.,'空间')]")
ActionChains(dr).move_to_element(kj).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'学校空间')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('校本资源').click()
time.sleep(mintime)
dr.find_element_by_link_text('学校简介').click()
time.sleep(mintime)
dr.find_element_by_link_text('名师风采').click()
time.sleep(mintime)
dr.find_element_by_link_text('学校教师').click()
time.sleep(mintime)
dr.find_element_by_link_text('班级空间').click()
time.sleep(mintime)
dr.find_element_by_link_text('主页').click()
time.sleep(mintime)
dr.find_element_by_css_selector('.instback').click()#返回首页
dr.implicitly_wait(waittime)
#首页-空间-班级空间
kj = dr.find_element_by_xpath("//span[contains(.,'空间')]")
ActionChains(dr).move_to_element(kj).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'班级空间')]").click()
time.sleep(mintime)
dr.find_element_by_css_selector('.instback').click()#返回首页
dr.implicitly_wait(waittime)
#首页-空间-个人空间
kj = dr.find_element_by_xpath("//span[contains(.,'空间')]")
ActionChains(dr).move_to_element(kj).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'个人空间')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('我的私信').click()
time.sleep(mintime)
dr.find_element_by_link_text('我的问答').click()
time.sleep(mintime)
dr.find_element_by_link_text('系统消息').click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/header/div/div/div/div").click()#返回首页
dr.implicitly_wait(waittime)



#导航社区点击
dr.find_element_by_xpath("//span[contains(.,'社区')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('最新').click()
time.sleep(mintime)
dr.find_element_by_link_text('浏览量').click()
dr.find_element_by_link_text('首页').click()#返回首页
dr.implicitly_wait(waittime)


#首页-统计-课堂数据
tj = dr.find_element_by_xpath("//span[contains(.,'统计')]")
ActionChains(dr).move_to_element(tj).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'课堂数据')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('用户统计').click()
time.sleep(mintime)
dr.find_element_by_link_text('资源统计').click()
time.sleep(mintime)
dr.find_element_by_link_text('教学统计').click()
time.sleep(mintime)
dr.find_element_by_link_text('教研统计').click()
time.sleep(mintime)
dr.find_element_by_link_text('活动统计').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-统计-用户统计
tj = dr.find_element_by_xpath("//span[contains(.,'统计')]")
ActionChains(dr).move_to_element(tj).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'用户统计')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-统计-活动统计
tj = dr.find_element_by_xpath("//span[contains(.,'统计')]")
ActionChains(dr).move_to_element(tj).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'活动统计')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-统计-数据监控
tj = dr.find_element_by_xpath("//span[contains(.,'统计')]")
ActionChains(dr).move_to_element(tj).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'数据监控')]").click()
time.sleep(mintime)
dr.back()
dr.implicitly_wait(waittime)

#导航活动点击
dr.find_element_by_xpath("//span[contains(.,'活动')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('发现活动').click()
time.sleep(mintime)
dr.find_element_by_link_text('我的活动').click()
time.sleep(mintime)
dr.find_element_by_link_text('活动首页').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)


#首页-菜单-系统消息
list = dr.find_element_by_css_selector('.glyphicon-list')
ActionChains(dr).move_to_element(list).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'系统消息')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/header/div/div/div/div").click()#返回首页
dr.implicitly_wait(waittime)
#首页-菜单-我的私信
list = dr.find_element_by_css_selector('.glyphicon-list')
ActionChains(dr).move_to_element(list).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'我的私信')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/header/div/div/div/div").click()#返回首页
dr.implicitly_wait(waittime)
#首页-菜单-@提到我的
list = dr.find_element_by_css_selector('.glyphicon-list')
ActionChains(dr).move_to_element(list).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'@提到我的')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('我的圈子').click()
time.sleep(mintime)
dr.find_element_by_link_text('提到我的').click()
time.sleep(mintime)
dr.find_element_by_link_text('好友/关注/粉丝').click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/header/div/div/div/div").click()#返回首页
dr.implicitly_wait(waittime)


#导航用户名点击
dr.find_element_by_css_selector('.uname').click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/header/div/div/div/div").click()#返回首页
dr.implicitly_wait(waittime)

#首页中部导航-教研中心
dr.find_element_by_link_text('教研会商').click()
time.sleep(mintime)
dr.find_element_by_link_text('首页').click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('教研管理').click()
time.sleep(mintime)
dr.find_element_by_link_text('首页').click()#浏览器回首页
time.sleep(mintime)
#首页中部导航-教学中心
dr.find_element_by_link_text('智慧课堂').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('导学案').click()
time.sleep(mintime)
#首页中部导航-社区中心
dr.find_element_by_link_text('学校空间').click()
time.sleep(mintime)
dr.find_element_by_css_selector('.instback').click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('班级空间').click()
time.sleep(mintime)
dr.find_element_by_css_selector('.instback').click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('个人空间').click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/header/div/div/div/div").click()#浏览器回首页
time.sleep(mintime)
#首页中部导航-资源中心
dr.find_element_by_link_text('国家课程').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('我的资源').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#浏览器回首页
time.sleep(mintime)
#首页中部导航-数据管理
dr.find_element_by_link_text('课堂数据').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('学业数据').click()
time.sleep(mintime)
dr.find_element_by_link_text('行规数据').click()
time.sleep(mintime)
dr.find_element_by_link_text('教研数据').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#浏览器回首页
dr.implicitly_wait(waittime)

#首页-用户名-个人中心
uname = dr.find_element_by_css_selector('.uname')
ActionChains(dr).move_to_element(uname).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'个人中心')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/div/div/div/div/div").click()#返回首页
dr.implicitly_wait(waittime)
#首页-用户名-个人中心
uname = dr.find_element_by_css_selector('.uname')
ActionChains(dr).move_to_element(uname).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'退出')]").click()
dr.implicitly_wait(waittime)



dr.close()