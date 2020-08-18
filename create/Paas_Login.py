from create.Smart_Waiting import waitutil
class Loginfor():

    # 封装
    def __init__(self, driver):
        self.driver = driver
        self.waitutil = waitutil(self.driver)  # 实例化WaitUtil类
    def login(self, username, password):
        self.waitutil.visibility_of_element_located('css', '.glyphicon-login', 30, 0.3).click()
        self.waitutil.visibility_of_element_located('id', 'login-name', 30, 0.3).send_keys(username)
        self.waitutil.visibility_of_element_located('id', 'login-pwd', 30, 0.3).send_keys(password)
        self.waitutil.visibility_of_element_located('css', '.btnlogin', 30, 0.3).click()
