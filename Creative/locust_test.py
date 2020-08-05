#0、导入相关模块
from locust import HttpLocust, TaskSet, task, between

#1、创建任务&任务集
# 需要继承TaskSet父类
class UserBehavior(TaskSet):


    #在on_start方法中，定义用例的前置
    #setup
    #在任务执行之前，会自动调用
    #名称固定
    #on_stop


    def on_start(self):

        url = '/AccountService.asmx/LoginAccountJson'
        logindata = {"account": "sqa06s77",
                     "password": "123456",
                     "page": "0"
                     }
        headers = {'Host': 'test.ws.forclass.net'}
        #发送post请求并得到响应
        self.client.post(url, headers=headers, data=logindata, name='登录')

        #client对象，是requests请求库中的HttpSession对象（有拓展）
        #可以类比为浏览器
        #会返回一个Response对象


    #需要使用#task来装饰实例方法，会作为一个任务来执行
    @task
    def GetSCStudentAssignmentList(self):
        url = 'ANAService.asmx/GetSCStudentAssignmentList'
        headers_dict = {
            'Host': 'test.ws.forclass.net',
            'Connection': 'keep-alive',
            'Content-Length': '65',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'http://test.forclass.net',
            'Referer': 'http://test.forclass.net/Account/SignIn',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }
        self.client.get("url, headers=headers_dict")

#创建模拟用户
#需要继承HttpLocust父类
class WebsiteUser(HttpLocust):
    #需要使用task_set类属性来制定当前用户要执行的任务
    #指定的任务，可以是TaskSet子类、列表(TaskSet子类)、字典
    task_set = UserBehavior
    #使用来制定任务执行的间隔
    #默认单位为秒
    #between函数，第一个参数为等候的最小时间，第二个参数为等候的最大时间
    wait_time = between(1,2)

    #min_wait = 3000
    #max_wait = 6000



