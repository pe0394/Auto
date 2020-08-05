from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

dr = webdriver.Chrome('d:\chromedriver.exe')
dr.maximize_window()

dr.get('http:\\paas.forclass.net')
waittime = 30
mintime = 3
dr.implicitly_wait(waittime)


#学生操作
#首页登录按钮
dr.find_element_by_css_selector('.glyphicon-login').click()
#输入账号
login = dr.find_element_by_id('login-name')
login.send_keys('sqa01s01')
#输入密码
pwd = dr.find_element_by_id('login-pwd')
pwd.send_keys('666666')
#登录按钮
dr.find_element_by_css_selector('.btnlogin').click()
time.sleep(5)

#导航资源点击
dr.find_element_by_xpath("//span[contains(.,'资源')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-资源-微课视频
zy = dr.find_element_by_xpath("//span[contains(.,'资源')]")
ActionChains(dr).move_to_element(zy).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'微课视频')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-资源-数字阅读
zy = dr.find_element_by_xpath("//span[contains(.,'资源')]")
ActionChains(dr).move_to_element(zy).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'数字阅读')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-资源-虚拟实验
zy = dr.find_element_by_xpath("//span[contains(.,'资源')]")
ActionChains(dr).move_to_element(zy).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'虚拟实验')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'DIY实验')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'经典实验')]").click()
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
#首页-教学-作业系统
jx = dr.find_element_by_xpath("//span[contains(.,'教学')]")
ActionChains(dr).move_to_element(jx).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'作业系统')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('自主训练').click()
time.sleep(mintime)
dr.find_element_by_link_text('错题本').click()
time.sleep(mintime)
dr.find_element_by_link_text('好题本').click()
time.sleep(mintime)
dr.find_element_by_link_text('统计分析').click()
time.sleep(mintime)
dr.find_element_by_link_text('我的成长').click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/div/div/div/div/div").click()#返回首页
dr.implicitly_wait(waittime)
#首页-教学-家校通
jxt = dr.find_element_by_xpath("//li[contains(.,'家校通')]")
ActionChains(dr).move_to_element(jxt).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'家校通')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)

#导航空间点击
dr.find_element_by_xpath("//span[contains(.,'空间')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//a[contains(text(),'教师')]").click()
time.sleep(mintime)
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
dr.find_element_by_link_text('我的私信').click()
time.sleep(mintime)
dr.find_element_by_link_text('班级消息').click()
time.sleep(mintime)
dr.find_element_by_link_text('我的问答').click()
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
time.sleep(mintime)
dr.find_element_by_link_text('浏览量').click()
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

#导航活动点击
dr.find_element_by_xpath("//span[contains(.,'活动')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('发现活动').click()
time.sleep(mintime)
dr.find_element_by_link_text('我的活动').click()
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

#首页中部导航-资源中心
dr.find_element_by_link_text('同步资源').click()
time.sleep(mintime)
dr.find_element_by_link_text('微课视频').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('数字阅读').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('教学应用').click()
time.sleep(mintime)
#首页中部导航-教学中心
dr.find_element_by_link_text('智慧课堂').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('在线课堂').click()
time.sleep(mintime)
dr.find_element_by_link_text('作业系统').click()
time.sleep(5)
dr.find_element_by_xpath("//div[@id='header']/div/div/div/div/div").click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('家校通').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#浏览器回首页#浏览器回首页
time.sleep(mintime)
#首页中部导航-训研中心
dr.find_element_by_link_text('集体备课').click()
time.sleep(mintime)
dr.find_element_by_link_text('录播评课').click()
time.sleep(mintime)
dr.find_element_by_link_text('主题研讨').click()
time.sleep(mintime)
dr.find_element_by_link_text('名师课堂').click()
time.sleep(mintime)
dr.find_element_by_link_text('一师一优课').click()
time.sleep(mintime)
#首页中部导航-空间社区
dr.find_element_by_link_text('个人空间').click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/header/div/div/div/div").click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('教育空间').click()
time.sleep(5)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('教育社区').click()
time.sleep(mintime)
dr.find_element_by_link_text('首页').click()#浏览器回首页
time.sleep(mintime)
#首页中部导航-数据管理
dr.find_element_by_link_text('平台管理').click()
time.sleep(mintime)
dr.find_element_by_link_text('数据分析').click()
time.sleep(mintime)


#导航用户名点击
dr.find_element_by_css_selector('.uname').click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/header/div/div/div/div").click()#返回首页
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