from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

# appium服务器初始化参数
desired_cap = {}
# 设备信息
desired_cap['platformName'] = 'Android'  # 平台的名称
desired_cap['deviceName'] = 'emulator-5554'  # 设备adb devices号
desired_cap['automationName'] = 'UiAutomator2'
# app信息
desired_cap['appPackage'] = 'com.gumi.spokenenglish'  # app包名
desired_cap['appActivity'] = 'com.gumi.spokenenglish.activity.LogoActivity'  # app欢迎页
desired_cap['autoGrantPermissions'] = 'true'  # 自动处理权限弹框

# 声明driver对象，连接appium server,并发送给它设备信息
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
driver.implicitly_wait(10)

# 服务协议隐私
driver.find_element_by_id('com.gumi.spokenenglish:id/permission_btn').click()
# 跳过
driver.find_element_by_id('com.gumi.spokenenglish:id/tv_guide_skip').click()
# actions = TouchAction(driver)
# actions.tap_and_hold(20,20)
# actions.move_to(10,100)
# actions.release()
# actions.perform()
sleep(2)
TouchAction(driver).press(x=733, y=2352).move_to(x=740, y=1143).release().perform()  # 屏幕坐标滑动

sleep(3)
# 我的
driver.find_element_by_id('com.gumi.spokenenglish:id/radio_mine').click()
# 右上角登录按钮
driver.find_element_by_id('com.gumi.spokenenglish:id/btn_login').click()
# 密码登录
driver.find_element_by_id('com.gumi.spokenenglish:id/account_txt').click()

username = driver.find_element_by_id('com.gumi.spokenenglish:id/login_username')
username.send_keys('18081840862')
sleep(1)
pwd = driver.find_element_by_id('com.gumi.spokenenglish:id/login_password')
pwd.send_keys('12345678')
sleep(1)
# 登录按钮
driver.find_element_by_id('com.gumi.spokenenglish:id/login_login').click()
driver.implicitly_wait(20)
# 首页
driver.find_element_by_id('com.gumi.spokenenglish:id/radio_home').click()
driver.implicitly_wait(20)
# 选择教材3年级上pep
driver.find_element_by_id('com.gumi.spokenenglish:id/btn_right').click()
sleep(1)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView").click()
# 教材听力
driver.find_element_by_id('com.gumi.spokenenglish:id/listening_book_layout').click()
driver.implicitly_wait(20)
# 点击图片区域播放
driver.find_element_by_id('com.gumi.spokenenglish:id/section_status').click()
sleep(3)
# 下一曲
el1 = driver.find_element_by_id("com.gumi.spokenenglish:id/next_btn")
el1.click()
sleep(10)
# 暂停
stop = driver.find_element_by_id('com.gumi.spokenenglish:id/play_btn')
stop.click()
driver.implicitly_wait(3)
# 左上角返回
back = driver.find_element_by_id('com.gumi.spokenenglish:id/back_btn')
back.click()
driver.implicitly_wait(3)

# 第5个播放按钮
driver.find_element_by_xpath('//android.widget.ExpandableListView[@resource-id=\"com.gumi.spokenenglish:id/expand_listview\"]/android.widget.LinearLayout[6]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageButton[1]').click()
sleep(2)
# 暂停
stop.click()
sleep(2)
# 左上角返回
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ImageButton[1]").click()
driver.implicitly_wait(3)

# 单词
driver.find_element_by_id('com.gumi.spokenenglish:id/word_layout').click()

driver.find_element_by_id('com.gumi.spokenenglish:id/btn_vocabulary').click()

driver.find_element_by_id('com.gumi.spokenenglish:id/andio_btn').click()

# 退出程序不关闭服务
driver.quit()








