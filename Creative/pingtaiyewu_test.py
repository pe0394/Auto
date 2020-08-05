from selenium import webdriver
import time
import pyperclip    #读写剪贴板(windows)
import win32api     #导入模拟键盘操作
import win32con     #导入控制键盘

class Testpingtaiyewu:
    def setup(self):
        self.driver = webdriver.Chrome('d:\\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('http:\\paas.forclass.net')
        self.driver.implicitly_wait(20)

    def test_1(self):

        # 定义函数为 作业链接，如果作业链接找不到，点击下一页查找，直到找到链接
        def find_elemet_by_link_text(key):
            try:
                ele = self.driver.find_element_by_link_text(key)  # 根据key值获取元素
                return ele  # 如果dr.find_element_by_link_text不出现异常，就会执行这句话，并返回element元素。如果报异常，这句话不执行，直接到异常处理
            except Exception as e:
                print(e)  # 如果dr.find_element_by_link_text报异常，会到这里，然后执行打印
                return None  # 然后执行返回

        def find_element_by_css_selector(key):
            try:
                ele = self.driver.find_element_by_css_selector(key)
                return ele
            except Exception as e:
                print(e)
                return None

        def find_element_by_xpath(key):
            try:
                ele = self.driver.find_element_by_xpath(key)
                return ele
            except Exception as e:
                print(e)
                return None

        def find_element_by_id(key):
            try:
                ele = self.driver.find_element_by_id(key)
                return ele
            except Exception as e:
                print(e)
                return None

# self.driver = webself.driveriver.Chrome('H:\\auto\chromeself.driveriver.exe')
# self.driver.maximize_window()
#
# self.driver.get('http:\\paas.forclass.net')
# waittime = 10
# mintime = 3
# self.driver.implicitly_wait(waittime)
#教师操作
#首页登录按钮
        self.driver.find_element_by_css_selector('.glyphicon-login').click()

        #输入账号
        login = self.driver.find_element_by_id('login-name')
        login.send_keys('sqa001')
        #输入密码
        pwd = self.driver.find_element_by_id('login-pwd')
        pwd.send_keys('654321')
        #登录按钮
        self.driver.find_element_by_css_selector('.btnlogin').click()
        time.sleep(5)

        #点击教研
        self.driver.find_element_by_xpath('//span[contains(text(),"教研")]').click()
        time.sleep(3)

    #自主备课
        def zizhubeike():
            self.driver.find_element_by_xpath('//a[contains(text(),"自主备课")]').click()
            time.sleep(5)
            #创建自主备课
            self.driver.find_element_by_xpath('//span[contains(text(),"我要备课")]').click()
            #添加章节
            self.driver.find_element_by_xpath('//span[contains(text(),"添加章节")]').click()
            self.driver.find_element_by_xpath('//span[contains(text(),"天地人")]').click()
            self.driver.find_elements_by_xpath('//span[contains(text(),"确定")]')[2].click()
            time.sleep(1)
            #输入标题
            self.driver.find_element_by_css_selector('[placeholder="请输入作品名称"]').send_keys('测试输入作品名称')
            # 非input标签上传文件
            pyperclip.copy(r"H:\auto\test.png")  # 复制文件路径到剪切板，pyperclip库需要安装
            # 点击活动页面上传封面按钮
            self.driver.find_element_by_css_selector('[class="uploadBox"]').click()
            time.sleep(1)
            # 发送 ctrl（17） + V（86）按钮
            win32api.keybd_event(17, 0, 0, 0)
            win32api.keybd_event(86, 0, 0, 0)
            win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
            win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(1)
            win32api.keybd_event(13, 0, 0, 0)  # (回车)
            win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
            time.sleep(1)
           #教学设计起名字
            self.driver.find_element_by_css_selector('[placeholder="请输入内容"]').send_keys('测试教学设计')
            #添加资源
            self.driver.find_element_by_xpath('//span[contains(text(),"相关资源")]').click()
            self.driver.find_elements_by_xpath('//span[text()="添加"]')[0].click()
            self.driver.find_elements_by_xpath('//span[contains(text(),"确定")]')[0].click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//span[contains(text(),"提交")]').click()
            time.sleep(5)
            #预览
            self.driver.find_element_by_xpath(' //div[contains(text(),"测试输入作品名称")]').click()
            time.sleep(1)
            #评论
            #切换iframe
            iframe = self.driver.find_element_by_css_selector('[class="cke_wysiwyg_frame cke_reset"]')
            self.driver.switch_to.frame(iframe)
            shukuang = self.driver.find_element_by_tag_name('p') #评论
            shukuang.send_keys("我要大声叫三声：好好好")
            #释放iframe
            self.driver.switch_to.default_content()
            #点击发表
            self.driver.find_element_by_xpath('//span[contains(text(),"发表")]').click()
            time.sleep(3)
            #点击返回
            self.driver.find_element_by_css_selector('[class="el-icon-back"]').click()
            time.sleep(3)
            #共享
            self.driver.find_elements_by_xpath('//span[text()="共享"]')[0].click()
            time.sleep(1)
            self.driver.find_elements_by_css_selector('[class="el-radio__inner"]')[1].click()
            #点击确定
            self.driver.find_elements_by_xpath('//span[contains(text(),"确定")]')[0].click()
            time.sleep(3)
            #撤回共享
            self.driver.find_elements_by_xpath('//span[contains(text(),"撤回")]')[0].click()
            #分享
            self.driver.find_elements_by_xpath('//span[contains(text(),"分享")]')[0].click()
            time.sleep(3)
            #选择成员全选
            self.driver.find_elements_by_xpath('//span[contains(text(),"全选")]')[0].click()
            #点击确定
            self.driver.find_elements_by_xpath('//span[contains(text(),"确定")]')[1].click()
            time.sleep(3)
            #收藏
            self.driver.find_elements_by_xpath('//span[text()="收藏"]')[0].click()
            #删除
            self.driver.find_elements_by_xpath('//span[text()="删除"]')[0].click()
            #确定
            self.driver.find_elements_by_xpath('//span[contains(text(),"确定")]')[2].click()
            time.sleep(2)
            #搜索备课
            self.driver.find_element_by_css_selector('[placeholder="请输入优课名称"]').send_keys('测试输入')
            self.driver.find_element_by_css_selector('[class="el-icon-search"]').click()

            zizhubeike()
    def teardown(self):
         pass