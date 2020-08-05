from create import WebFindWait
class Loginfor():

    # 封装
    def __init__(self, driver):
        self.driver = driver
        self.waitUtil = WebFindWait.WaitUtil(self.driver)  # 实例化WaitUtil类
    def login(self, username, password):
        self.waitUtil.find_element('css', '.glyphicon-login', 30, 0.3).click()
        self.waitUtil.find_element('id', 'login-name', 30, 0.3).send_keys(username)
        self.waitUtil.find_element('id', 'login-pwd', 30, 0.3).send_keys(password)
        self.waitUtil.find_element('css', '.btnlogin', 30, 0.3).click()
