from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

dr = webdriver.Chrome('d:\chromedriver.exe')
dr.maximize_window()

dr.get('http:\\paas.forclass.net')
waittime = 30
mintime = 3
dr.implicitly_wait(waittime)

#管理员操作
#首页登录按钮
dr.find_element_by_css_selector('.glyphicon-login').click()
#输入账号
login = dr.find_element_by_id('login-name')
login.send_keys('sqa-adm01')
#输入密码
pwd = dr.find_element_by_id('login-pwd')
pwd.send_keys('ABCabc01')
#登录按钮
dr.find_element_by_css_selector('.btnlogin').click()
time.sleep(5)

#导航资源点击
dr.find_element_by_xpath("//span[contains(.,'资源')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-资源-同步资源
zy = dr.find_element_by_xpath("//span[contains(.,'资源')]")
ActionChains(dr).move_to_element(zy).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'同步资源')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('教学应用').click()
time.sleep(mintime)
dr.find_element_by_link_text('我的资源').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-资源-教学应用
zy = dr.find_element_by_xpath("//span[contains(.,'资源')]")
ActionChains(dr).move_to_element(zy).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'教学应用')]").click()
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
#首页-教学-在线课堂
jx = dr.find_element_by_xpath("//span[contains(.,'教学')]")
ActionChains(dr).move_to_element(jx).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'在线课堂')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//a[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-教学-家校通
jxt = dr.find_element_by_xpath("//li[contains(.,'家校通')]")
ActionChains(dr).move_to_element(jxt).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'家校通')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)

#导航教研点击
dr.find_element_by_xpath("//span[contains(.,'教研')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('自主备课').click()
time.sleep(mintime)
dr.find_element_by_link_text('集体备课').click()
time.sleep(mintime)
dr.find_element_by_link_text('录播评课').click()
time.sleep(mintime)
dr.find_element_by_link_text('主题研讨').click()
time.sleep(mintime)
dr.find_element_by_link_text('问卷调查').click()
time.sleep(mintime)
dr.find_element_by_link_text('投票活动').click()
time.sleep(mintime)
dr.find_element_by_link_text('在线课堂').click()
time.sleep(mintime)
dr.find_element_by_link_text('优化作业').click()
time.sleep(mintime)
dr.find_element_by_link_text('一师一优课').click()
time.sleep(mintime)
dr.find_element_by_link_text('其他活动').click()
time.sleep(mintime)
dr.find_element_by_link_text('教研组').click()
time.sleep(mintime)
dr.find_element_by_link_text('首页').click()#返回首页
time.sleep(mintime)
#首页-教研-集体备课
jy = dr.find_element_by_xpath("//span[contains(.,'教研')]")
ActionChains(dr).move_to_element(jy).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'集体备课')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('首页').click()#返回首页
dr.implicitly_wait(waittime)
#首页-教研-录播评课
jy = dr.find_element_by_xpath("//span[contains(.,'教研')]")
ActionChains(dr).move_to_element(jy).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'录播评课')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('首页').click()#返回首页
dr.implicitly_wait(waittime)
#首页-教研-主题研讨
jy = dr.find_element_by_xpath("//span[contains(.,'教研')]")
ActionChains(dr).move_to_element(jy).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'主题研讨')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('首页').click()#返回首页
dr.implicitly_wait(waittime)
#首页-教研-一师一优课
jy = dr.find_element_by_xpath("//span[contains(.,'教研')]")
ActionChains(dr).move_to_element(jy).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'一师一优课')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('首页').click()#返回首页
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
dr.find_element_by_link_text('系统消息').click()
time.sleep(mintime)
dr.find_element_by_xpath("//div[@id='header']/header/div/div/div/div").click()#返回首页
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

#首页-管理-账户管理
gl = dr.find_element_by_xpath("//span[contains(.,'管理')]")
ActionChains(dr).move_to_element(gl).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'账户管理')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('班级管理').click()
time.sleep(mintime)
dr.find_element_by_link_text('角色管理').click()
time.sleep(mintime)
dr.find_element_by_link_text('教师管理').click()
time.sleep(mintime)
dr.find_element_by_link_text('学生管理').click()
time.sleep(mintime)
dr.find_element_by_link_text('家长管理').click()
time.sleep(mintime)
dr.find_element_by_link_text('邀请码管理').click()
time.sleep(mintime)
dr.find_element_by_link_text('学校管理').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)

#首页-管理-资源管理
gl = dr.find_element_by_xpath("//span[contains(.,'管理')]")
ActionChains(dr).move_to_element(gl).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'资源管理')]").click()
time.sleep(mintime)
dr.find_element_by_link_text('教材管理').click()
time.sleep(mintime)
dr.find_element_by_link_text('资源入库审核').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)
#首页-管理-教研管理
gl = dr.find_element_by_xpath("//span[contains(.,'管理')]")
ActionChains(dr).move_to_element(gl).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'教研管理')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)

#首页-管理-设备管理
gl = dr.find_element_by_xpath("//span[contains(.,'管理')]")
ActionChains(dr).move_to_element(gl).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'设备管理')]").click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#返回首页
dr.implicitly_wait(waittime)


#首页-统计-统计分析
tj = dr.find_element_by_xpath("//span[contains(.,'统计')]")
ActionChains(dr).move_to_element(tj).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'统计分析')]").click()
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
#首页-统计-监控数据
tj = dr.find_element_by_xpath("//span[contains(.,'统计')]")
ActionChains(dr).move_to_element(tj).perform()
time.sleep(mintime)
dr.find_element_by_xpath("//li[contains(.,'监控数据')]").click()
time.sleep(mintime)
dr.back()#浏览器回首页
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

#首页中部导航-资源中心
dr.find_element_by_link_text('同步资源').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#浏览器回首页
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
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#浏览器回首页
time.sleep(mintime)
#首页中部导航-教学中心
dr.find_element_by_link_text('智慧课堂').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('在线课堂').click()
time.sleep(mintime)
dr.find_element_by_link_text('首页').click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('作业系统').click()
time.sleep(mintime)
dr.find_element_by_link_text('家校通').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#浏览器回首页#浏览器回首页
time.sleep(mintime)
#首页中部导航-教研中心
dr.find_element_by_link_text('集体备课').click()
time.sleep(mintime)
dr.find_element_by_link_text('首页').click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('录播评课').click()
time.sleep(mintime)
dr.find_element_by_link_text('首页').click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('主题研讨').click()
time.sleep(mintime)
dr.find_element_by_link_text('首页').click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('名师课堂').click()
time.sleep(mintime)
dr.find_element_by_link_text('一师一优课').click()
time.sleep(mintime)
dr.find_element_by_link_text('首页').click()#浏览器回首页
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
dr.find_element_by_xpath("//div[@id='app']/div/div/nav/div/div[2]/ul/li/span").click()#浏览器回首页
time.sleep(mintime)
dr.find_element_by_link_text('数据分析').click()
time.sleep(mintime)
dr.find_element_by_xpath("//span[contains(.,'首页')]").click()#浏览器回首页
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