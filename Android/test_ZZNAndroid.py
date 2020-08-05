from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestZZN:
    def setup(self):
        # appium服务器初始化参数
        desired_cap = {}
        # 设备信息
        desired_cap['platformName'] = 'Android'  # 平台的名称
        desired_cap['deviceName'] = 'HuaWei'  # 设备adb devices号
        # app信息
        desired_cap['appPackage'] = 'com.zhizhiniao'  # app包名
        desired_cap['appActivity'] = 'com.zhizhiniao.view.LoginActivity'  # app欢迎页
        desired_cap["autoGrantPermissions"] = 'true'  # 自动处理权限弹框
        # 声明driver对象，连接appium server,并发送给它设备信息
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(10)

    def test_login(self):
        # 登录
        username = self.driver.find_element_by_id('com.zhizhiniao:id/login_et_account')
        username.send_keys('cexsun0102')
        pwd = self.driver.find_element_by_id('com.zhizhiniao:id/login_et_password')
        pwd.send_keys('123477')
        self.driver.find_element_by_id('com.zhizhiniao:id/login_btn_login').click()  # 登录按钮

        #引导页
        self.driver.find_element_by_id('com.zhizhiniao:id/hint_page_confirm_btn').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.zhizhiniao:id/question_child_mic_btn').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        time.sleep(1)

        mic = self.driver.find_element_by_id('com.zhizhiniao:id/audio_recoder_mic_action')
        TouchAction(self.driver).press(mic).wait(3610000).release().perform()  # 按下蓝牙按钮，等待3秒，并释放#按下说话按钮不放

    def test_gsm_call(self):
        self.driver.make_gsm_call('13719809283', GsmCallActions.CALL)  # 模拟打电话

    def teardown(self):
        pass
        # 退出程序不关闭服务
        #self.driver.quit()



