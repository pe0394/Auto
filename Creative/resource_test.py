from selenium import webdriver
import time
import win32api
import win32con
import pyperclip


class TestResource:
    def setup(self):
        self.driver = webdriver.Chrome('d:\\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('http:\\paas.forclass.net')
        self.driver.implicitly_wait(20)

    def login(self):
        # 教师操作
        # 首页登录按钮
        self.driver.find_element_by_css_selector('.glyphicon-login').click()
        # 输入账号
        login = self.driver.find_element_by_id('login-name')
        login.send_keys('sqa001')
        # 输入密码
        pwd = self.driver.find_element_by_id('login-pwd')
        pwd.send_keys('654321')
        # 登录按钮
        self.driver.find_element_by_css_selector('.btnlogin').click()

        # 定义函数为 作业链接，如果作业链接找不到，点击下一页查找，直到找到链接
    def find_element_by_link_text(self,key):
        try:
            ele = self.driver.find_element_by_link_text(key)  # 根据key值获取元素
            return ele  # 如果dr.find_element_by_link_text不出现异常，就会执行这句话，并返回element元素。如果报异常，这句话不执行，直接到异常处理
        except Exception as e:
            print(e)  # 如果dr.find_element_by_link_text报异常，会到这里，然后执行打印
            return None  # 然后执行返回

    def find_element_by_css_selector(self,key):
        try:
            ele = self.driver.find_element_by_css_selector(key)
            return ele
        except Exception as e:
            print(e)
            return None

    def find_elements_by_css_selector(self,key):
        try:
            ele = self.driver.find_elements_by_css_selector(key)
            return ele
        except Exception as e:
            print(e)
            return None

    def find_element_by_xpath(self,key):
        try:
            ele = self.driver.find_element_by_xpath(key)
            return ele
        except Exception as e:
            print(e)
            return None

    def find_element_by_id(self,key):
        try:
            ele = self.driver.find_element_by_id(key)
            return ele
        except Exception as e:
            print(e)
            return None

    # 进入同步资源
    def find_Resourcecenter(self):
        # 创建
        element = self.find_element_by_link_text('同步资源')
        if (element == None):
            self.driver.find_element_by_link_text('同步资源').click()
            time.sleep(1)
            self.find_Resourcecenter()
        else:
            element.click()

    def test_1(self):#资源中心创建教学资源，数字试题，教学应用，互动微课

        def find_create():
            # 创建
            element = self.find_element_by_css_selector('.ivu-icon-compose')
            if (element == None):
                self.driver.find_element_by_css_selector('.ivu-icon-compose').click()
                time.sleep(1)
                find_create()
            else:
                element.click()

        def upload_file():
            # 发送 ctrl（17） + V（86）按钮
            win32api.keybd_event(17, 0, 0, 0)
            win32api.keybd_event(86, 0, 0, 0)
            win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
            win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(1)
            win32api.keybd_event(13, 0, 0, 0)  # (回车)
            win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
            time.sleep(3)

        def ziyuan():
            #教学资源标签
            #非input标签上传文件
            pyperclip.copy("D:\\test.jpg")  # 复制文件路径到剪切板，pyperclip库需要安装
            self.driver.find_element_by_css_selector('.upload-prompt-text').click()
            time.sleep(3)  # 等待程序加载 时间 看你电脑的速度 单位(秒)

            upload_file()
            time.sleep(3)
            #发送文字
            jianjie = self.driver.find_element_by_css_selector('[wrap="soft"][autocomplete="off"]')
            jianjie.send_keys('等待程序加载 时间 看你电脑的速度 单位')
            time.sleep(1)

            # 选择目录
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div/i').click()
            self.driver.find_element_by_xpath("//li[text()='初中']").click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div/i').click()
            self.driver.find_element_by_xpath("//li[text()='语文']").click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div/i').click()
            self.driver.find_element_by_xpath("//li[text()='统编版']").click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div/i').click()
            self.driver.find_element_by_xpath("//li[text()='七年级上']").click()
            self.driver.find_element_by_css_selector('[class="ivu-icon ivu-icon-plus-circled"]').click()
            self.driver.find_element_by_xpath('//span[text()="2 济南的冬天"]').click()
            self.driver.find_element_by_css_selector('[class="ivu-btn ivu-btn-primary ivu-btn-large"]').click()

            time.sleep(3)
            #发布
            self.driver.find_element_by_xpath("//span[text()='发布']").click()


        self.login()


        # 资源中心
        self.find_Resourcecenter()
        time.sleep(3)
        find_create()

        ziyuan()

        time.sleep(3)

        find_create()
        time.sleep(3)

        # 数字试卷标签
        self.driver.find_element_by_xpath("//div[contains(text(),'数字试卷')]").click()
        #选择题型
        self.driver.find_element_by_css_selector('[title="2 济南的冬天"]').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('[title="单选题"]').click()
        #下一步
        #self.driver.find_element_by_css_selector('.cq-step1-next').click()
        #编辑试题
        # 切换iframe
        iframe = self.driver.find_element_by_css_selector('[id="ueditor_0"]')
        self.driver.switch_to.frame(iframe)
        #答题要求
        element = self.driver.find_element_by_css_selector('.cq-require-input')
        element.send_keys('这是答题要求')
        #大题干
        element = self.driver.find_element_by_css_selector('.cq-tigan1-input')
        element.send_keys('这是大题干')
        #小题干
        element = self.driver.find_element_by_css_selector('.cq-tmpl-q-title')
        element.send_keys('这是小题干')
        #选项
        element = self.driver.find_elements_by_css_selector('[class="form-control cq-option-input"]')[0]
        element.send_keys('这是选项A')
        element = self.driver.find_elements_by_css_selector('[class="form-control cq-option-input"]')[1]
        element.send_keys('这是选项B')
        element = self.driver.find_elements_by_css_selector('[class="form-control cq-option-input"]')[2]
        element.send_keys('这是选项C')
        element = self.driver.find_elements_by_css_selector('[class="form-control cq-option-input"]')[3]
        element.send_keys('这是选项D')
        #正确答案
        self.driver.find_elements_by_css_selector('.cq-op-checkbox')[0].click()
        #答案解析
        element = self.driver.find_element_by_css_selector('.cq-tmpl-textarea')
        element.send_keys('这是答案解析')
        #退出iframe
        self.driver.switch_to.default_content()
        #保存
        self.driver.find_element_by_css_selector('.cq-btn-save').click()
        #去我的题库
        self.driver.find_element_by_css_selector('.dlg-btn-submit').click()
        #首页
        self.driver.find_element_by_xpath("//div[text()='首页']").click()

        self.find_Resourcecenter()
        time.sleep(3)
        find_create()
        time.sleep(3)

        #教学应用标签
        self.driver.find_element_by_xpath("//div[contains(text(),'教学应用')]").click()
        self.driver.find_element_by_xpath("//span[contains(text(),'Android')]").click()
        self.driver.find_element_by_xpath("//span[contains(text(),'教学应用')]").click()
        self.driver.find_elements_by_css_selector('.ivu-checkbox-input')[6].click()
        self.driver.find_element_by_xpath("//span[contains(text(),'资源上传')]").click()
        # 非input标签上传文件
        pyperclip.copy("D:\\test.apk")  # 复制文件路径到剪切板，pyperclip库需要安装
        time.sleep(3)  # 等待程序加载 时间 看你电脑的速度 单位(秒)
        upload_file()
        time.sleep(3)  # 等待APK加载
        element = self.driver.find_element_by_css_selector('[placeholder="请输入资源名称"]')
        element.send_keys('我要打老虎')
        #上传资源图片
        self.driver.find_elements_by_css_selector('.ivu-icon-plus-round')[0].click()
        pyperclip.copy("D:\\test.jpg")  # 复制文件路径到剪切板，pyperclip库需要安装
        time.sleep(3)  # 等待程序加载 时间 看你电脑的速度 单位(秒)
        upload_file()

        self.driver.find_element_by_css_selector('[placeholder="应用名称（限400字）"]').click()
        self.driver.find_element_by_xpath("//span[contains(text(),'发布')]").click()
        #返回首页
        self.driver.find_element_by_xpath("//span[contains(text(),'首页')]").click()

        self.find_Resourcecenter()
        time.sleep(3)
        find_create()

        #互动微课标签
        self.driver.find_element_by_xpath("//div[contains(text(),'互动微课')]").click()
        time.sleep(1)
        self.driver.find_elements_by_css_selector('.ivu-select-arrow')[1].click()
        self.driver.find_element_by_xpath("//li[text()='初中']").click()
        self.driver.find_elements_by_css_selector('.ivu-select-arrow')[2].click()
        self.driver.find_element_by_xpath("//li[text()='语文']").click()
        self.driver.find_elements_by_css_selector('.ivu-select-arrow')[3].click()
        self.driver.find_element_by_xpath("//li[text()='统编版']").click()
        self.driver.find_elements_by_css_selector('.ivu-select-arrow')[4].click()
        self.driver.find_element_by_xpath("//li[text()='七年级上']").click()
        self.driver.find_element_by_xpath("//span[contains(text(),'添加章节')]").click()
        self.driver.find_element_by_xpath('//span[text()="2 济南的冬天"]').click()
        self.driver.find_element_by_css_selector('[class="ivu-btn ivu-btn-primary ivu-btn-large"]').click()
        self.driver.find_elements_by_xpath("//span[contains(text(),'确定')]")[0].click()
        self.driver.find_element_by_xpath("//span[contains(text(),'新建微课')]").click()
        time.sleep(5)
        #自由创建
        # 切换iframe
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="create-video"]/iframe'))
        self.driver.switch_to.frame("layui-layer-iframe2")
        self.driver.find_element_by_xpath("//div[contains(text(),'自由创建')]").click()
        #退到父级iframe，再退出iframe
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()
        #重新切换iframe
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="create-video"]/iframe'))
        #场景
        self.driver.find_elements_by_css_selector('.scImg')[0].click()
        #保存
        self.driver.find_element_by_id('moviesave').click()
        self.driver.switch_to.frame("layui-layer-iframe3")
        moviename = self.driver.find_element_by_css_selector('[placeholder="请输入影片名称"]')
        moviename.send_keys('小片子')
        self.driver.find_element_by_xpath("//button[contains(text(),'确定')]").click()
        time.sleep(5)#等待新建的微课加载

        #关闭
        self.driver.find_elements_by_css_selector(".ivu-icon-ios-close-empty")[26].click()
        self.driver.find_element_by_xpath("//span[contains(text(),'发布')]").click()


    def test_2(self):#同步资源，搜索，预览，评论，收藏，下载，分享


        self.login()
        self.find_Resourcecenter()
        time.sleep(3)
        #同步资源搜索
        def find_search_text1():
            element = self.find_element_by_css_selector('[placeholder="请输入资源关键字"]')
            if (element == None):
                self.driver.find_element_by_css_selector('[placeholder="请输入资源关键字"]')
                element.send_keys('小松鼠找花生')
                time.sleep(1)
                find_search_text1()
            else:
                element.send_keys('小松鼠找花生')

        def find_search_button():
            # 搜索按钮
            element = self.find_element_by_css_selector('.el-icon-search')
            if (element == None):
                self.driver.find_element_by_css_selector('.el-icon-search').click()
                time.sleep(1)
                find_search_button()
            else:
                element.click()

        find_search_text1()
        find_search_button()

        time.sleep(3)
        self.driver.back()

        #资源中心目录
        def resource_mulu():
            self.driver.find_element_by_css_selector('[class="pull-right ivu-icon ivu-icon-ios-arrow-right"]').click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//span[text()='初中']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//span[text()='语文']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//span[text()='统编版']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//span[text()='七年级上']").click()
            time.sleep(1)
            self.driver.find_element_by_css_selector('.ivu-btn-warning').click()

        resource_mulu()

        self.driver.find_element_by_xpath("//span[contains(text(),'我的创建')]").click()
        time.sleep(3)
        self.driver.find_elements_by_xpath("//span[contains(text(),'教学资源')]")[1].click()
        self.driver.find_element_by_xpath("//span[text()='test.jpg']").click()
        time.sleep(3)
        self.driver.find_element_by_css_selector('.ivu-icon-close-round').click()#关闭
        self.driver.find_element_by_xpath("//span[contains(text(),'数字试卷')]").click()
        self.driver.find_element_by_xpath("//span[text()='2 济南的冬天0621']").click()
        time.sleep(3)
        self.driver.find_element_by_css_selector('.ivu-icon-close-round').click()#关闭
        self.driver.find_element_by_xpath("//span[contains(text(),'数字试题')]").click()
        self.driver.find_element_by_xpath("//span[text()='试题2153290']").click()
        time.sleep(3)
        self.driver.find_element_by_css_selector('.ivu-icon-close-round').click()#关闭
        self.driver.find_element_by_xpath("//span[contains(text(),'教研资源')]").click()
        self.driver.find_element_by_xpath("//span[text()='2 济南的冬天lmm0623']").click()
        time.sleep(3)
        self.driver.find_element_by_css_selector('.ivu-icon-close-round').click()#关闭


        def find_collect():
            # 判断收藏状态，没有收藏点收藏，收藏了点取消
            ele1 = self.find_elements_by_css_selector('.ivu-icon-ios-heart-outline')[0]
            if(ele1 == None):
                self.driver.find_elements_by_css_selector('.ivu-icon-ios-heart')[0].click()
            else:
                ele1.click()
                self.driver.find_element_by_xpath('//span[text()="授课"]').click()

            ele2 = self.find_elements_by_css_selector('.ivu-icon-ios-heart')[0]
            if (ele2 == None):
                self.driver.find_elements_by_css_selector('.ivu-icon-ios-heart-outline')[0].click()
                self.driver.find_element_by_xpath('//span[text()="授课"]').click()
            else:
                ele2.click()

        find_collect()
        #切换教学资源
        self.driver.find_elements_by_xpath("//span[contains(text(),'教学资源')]")[1].click()
        #评论
        self.driver.find_elements_by_css_selector('.ivu-icon-ios-chatboxes-outline')[0].click()
        element = self.driver.find_element_by_css_selector('[placeholder="请输入评论......"]')
        element.send_keys('胃疼喝温水')
        self.driver.find_element_by_xpath("//span[text()='确定']").click()
        time.sleep(1)

        # 更多
        def find_more_button():
            element = self.find_elements_by_css_selector('[class="icon-gray list-icon"]')[0]
            if(element == None):
                self.driver.find_elements_by_css_selector('[class="icon-gray list-icon"]')[0].click()
                element.click()
                time.sleep(1)
                find_more_button()
            else:
                element.click()

        find_more_button()

        time.sleep(1)
        # 编辑
        self.driver.find_element_by_css_selector('[class="ivu-icon ivu-icon-ios-compose-outline"]').click()
        time.sleep(1)
        element = self.driver.find_element_by_css_selector('[placeholder="选项，简要介绍资源的主要内容，方便资源被更多人浏览和下载（不超过200字）"]')
        element.send_keys('AAAAAAA')
        # 发布
        self.driver.find_element_by_css_selector('[class="btn fb cursor"]').click()

        find_more_button()

        time.sleep(1)
        #删除
        self.driver.find_element_by_css_selector('[class="ivu-icon ivu-icon-trash-a"]').click()
        self.driver.find_elements_by_xpath("//span[contains(text(),'确定')]")[-1].click()
        #下载
        self.driver.find_elements_by_css_selector('.ivu-icon-ios-download-outline')[0].click()
        time.sleep(3)
        #分享
        self.driver.find_elements_by_css_selector('.ivu-icon-share')[0].click()
        self.driver.find_element_by_xpath('//label[contains(text(),"学生01")]').click()
        self.driver.find_element_by_xpath("//span[contains(text(),'分享')]").click()

        #精选
        self.driver.find_element_by_xpath("//span[contains(text(),'最新')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[contains(text(),'热度')]").click()
        time.sleep(1)
        self.driver.find_elements_by_xpath("//span[contains(text(),'评分')]")[0].click()
        time.sleep(1)
        #全站共享资源搜索

        self.driver.find_element_by_xpath("//span[contains(text(),'全站共享资源')]").click()

        def find_search_text2():
            element = self.find_element_by_css_selector('[placeholder="在结果中搜索"]')
            if(element == None):
                self.driver.find_element_by_css_selector('[placeholder="在结果中搜索"]')
                element.send_keys('1')
                time.sleep(1)
                find_search_text2()
            else:
                element.send_keys('1')

        def find_result_search():
            # 结果搜索按钮
            element = self.find_element_by_css_selector('.ivu-icon-ios-search-strong')
            if (element == None):
                self.driver.find_element_by_css_selector('.ivu-icon-ios-search-strong').click()
                time.sleep(1)
                find_result_search()
            else:
                element.click()
        find_search_text2()
        time.sleep(1)
        find_result_search()


        #教学应用
        def find_teaching_app():
            # 结果搜索按钮
            element = self.find_element_by_xpath("//a[text()='教学应用']")
            if (element == None):
                self.driver.find_element_by_xpath("//a[text()='教学应用']").click()
                time.sleep(1)
                find_teaching_app()
            else:
                element.click()
        find_teaching_app()


        self.driver.find_elements_by_xpath("//span[text()='我要打老虎']")[0].click()

        def find_appcollect():
            # 判断收藏状态，没有收藏点收藏，收藏了点取消
            ele1 = self.find_element_by_xpath('//span[text()="收藏"]')
            if (ele1 == None):
                self.driver.find_element_by_xpath('//span[text()="取消收藏"]').click()
            else:
                ele1.click()

            ele2 = self.find_element_by_xpath('//span[text()="取消收藏"]')
            if (ele2 == None):
                self.driver.find_element_by_xpath('//span[text()="收藏"]').click()
            else:
                ele2.click()

        find_appcollect()

        self.driver.find_element_by_xpath('//span[text()="下载到电脑"]').click()

        shuru = self.find_element_by_css_selector('[placeholder="评论不超过200字"]')
        shuru.send_keys('测试内容输入')
        time.sleep(1)
        self.driver.find_element_by_xpath('//span[text()="发布评论"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//span[text()="返回"]').click()

        #评论
        self.driver.find_elements_by_css_selector('.ivu-icon-ios-chatboxes-outline')[0].click()
        pinglun = self.driver.find_elements_by_css_selector('[placeholder="请输入评论......"]')[0]
        pinglun.send_keys('测试内容输入')
        self.driver.find_elements_by_xpath('//span[text()="确定"]')[0].click()

        #删除
        self.driver.find_elements_by_css_selector('.ivu-icon-trash-a')[0].click()
        self.driver.find_elements_by_xpath("//span[contains(text(),'确定')]")[-1].click()
        #精选
        self.driver.find_elements_by_xpath("//span[contains(text(),'评分')]")[0].click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[contains(text(),'收藏量')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[contains(text(),'浏览量')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[contains(text(),'最新')]").click()

    def teardown(self):
        # 退出
        pass
        #self.driver.close()
