from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestSE:
    def setup(self):
        # appium服务器初始化参数
        desired_cap = {}
        # 设备信息
        desired_cap['platformName'] = 'Android'  # 平台的名称
        desired_cap['deviceName'] = '192.168.189.101:5555'  # 设备adb devices号
        # app信息
        desired_cap['appPackage'] = 'com.gumi.spokenenglish'  # app包名
        desired_cap['appActivity'] = 'com.gumi.spokenenglish.activity.LogoActivity'  # app欢迎页
        desired_cap["autoGrantPermissions"] = 'true'  # 自动处理权限弹框
        desired_cap["unicodeKeyboard"] = 'true'
        # 声明driver对象，连接appium server,并发送给它设备信息
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(10)
    def test_SE(self):
        # 服务协议隐私
        self.driver.find_element_by_id('com.gumi.spokenenglish:id/permission_btn').click()
        sleep(2)
        # 跳过
        self.driver.find_element_by_id('com.gumi.spokenenglish:id/tv_guide_skip').click()
        # actions = TouchAction(driver)
        # actions.tap_and_hold(20,20)
        # actions.move_to(10,100)
        # actions.release()
        # actions.perform()
        #sleep(2)
        #TouchAction(self.driver).press(x=733, y=2352).move_to(x=740, y=1143).release().perform()  # 屏幕坐标滑动

        sleep(3)
        # 我的
        self.driver.find_element_by_id('com.gumi.spokenenglish:id/radio_mine').click()
        # 右上角登录按钮
        self.driver.find_element_by_id('com.gumi.spokenenglish:id/btn_login').click()
        # 密码登录
        self.driver.find_element_by_id('com.gumi.spokenenglish:id/account_txt').click()

        username = self.driver.find_element_by_id('com.gumi.spokenenglish:id/login_username')
        username.send_keys('18081840862')
        sleep(1)
        pwd = self.driver.find_element_by_id('com.gumi.spokenenglish:id/login_password')
        pwd.send_keys('12345678')
        sleep(1)
        # 登录按钮
        self.driver.find_element_by_id('com.gumi.spokenenglish:id/login_login').click()
        self.driver.implicitly_wait(20)
        #
        # # 首页
        # self.driver.find_element_by_id('com.gumi.spokenenglish:id/radio_home').click()
        # self.driver.implicitly_wait(20)
        # # 选择教材3年级上pep
        # self.driver.find_element_by_id('com.gumi.spokenenglish:id/btn_right').click()
        # sleep(1)
        # self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView").click()
        # # 教材听力
        # self.driver.find_element_by_id('com.gumi.spokenenglish:id/listening_book_layout').click()
        # self.driver.implicitly_wait(20)
        # # 点击图片区域播放
        # self.driver.find_element_by_id('com.gumi.spokenenglish:id/section_status').click()
        # sleep(3)
        # # 下一曲
        # el1 = self.driver.find_element_by_id("com.gumi.spokenenglish:id/next_btn")
        # el1.click()
        # sleep(10)
        # # 暂停
        # stop = self.driver.find_element_by_id('com.gumi.spokenenglish:id/play_btn')
        # stop.click()
        # self.driver.implicitly_wait(3)
        # # 左上角返回
        # back = self.driver.find_element_by_id('com.gumi.spokenenglish:id/back_btn')
        # back.click()
        # self.driver.implicitly_wait(3)
        #
        # # 第5个播放按钮
        # self.driver.find_element_by_xpath('//android.widget.ExpandableListView[@resource-id=\"com.gumi.spokenenglish:id/expand_listview\"]/android.widget.LinearLayout[6]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageButton[1]').click()
        # sleep(2)
        # # 暂停
        # stop.click()
        # sleep(2)
        # # 左上角返回
        # self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ImageButton[1]").click()
        # self.driver.implicitly_wait(3)
        #
        # # 单词
        # self.driver.find_element_by_id('com.gumi.spokenenglish:id/word_layout').click()
        #
        # self.driver.find_element_by_id('com.gumi.spokenenglish:id/btn_vocabulary').click()
        #
        # self.driver.find_element_by_id('com.gumi.spokenenglish:id/andio_btn').click()
    def test_gsm_call(self):
        self.driver.make_gsm_call('18801002028', GsmCallActions.CALL)
    def teardown(self):
        # 退出程序不关闭服务
        self.driver.quit()








