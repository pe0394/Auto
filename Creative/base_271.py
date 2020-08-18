from locust import HttpUser, task, between, SequentialTaskSet
from create import get_session
from create.log_result import loadLogger
import queue, csv, base64
from locust.contrib.fasthttp import FastHttpUser

class MySeqTasks(SequentialTaskSet):
    logindata = queue.Queue()
    with open(r'/test/username_271.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            logindata.put(row[0])
    logindata.task_done()

    # @task
    # def Userlogin(self):
    def on_start(self):
        account = self.logindata.get()
        try:
            account
        except queue.Empty:
            exit(0)
        url = 'http://webservice.forclass.net/ForClassService.asmx/Userlogin?'
        data = 'account=' + account + '&password=A3uM7sfoaOmELjcplxtocg==&xStr={"timestamp":"1595313434"}&typeIdx=1'
        with self.client.get(url + data, catch_response=True, name='登录') as response:
            if response.status_code == 200 and '<ReturnCode>0</ReturnCode>' in response.text:
                response.success()
                # print('登录成功' , response.text)
            else:
                response.failure()
                print('登录失败'+ response.text)
            self.session = get_session.getsession(response.text)
                # print(session)
        return self.session

    @task
    def category(self):
        str1 = "".join(self.session)
        bytes_session = str1.encode("utf-8")
        self.base_session = str(base64.b64encode(bytes_session), 'utf8')
        # print(self.base_session)
        url = 'http://api.forclass.net/Course/api/v1/Query/category'
        headers ={'Authorization':'Bearer '+self.base_session}
        data = {"keyword": "","pageIndex": 1,"pageSize": 19}
        with self.client.post(url, json=data, headers=headers, catch_response=True, name='获取用户的分类') as response:
            if response.status_code == 200 and 'retcode":0,' in response.text:
                response.success()
                # print('获取用户的分类成功'+ response.text)
            else:
                response.failure()
                print('获取用户的分类失败'+ response.text)

    @task
    def design(self):
        url = 'http://api.forclass.net/Course/api/v1/Query/design'
        headers ={'Authorization':'Bearer '+self.base_session}
        data = {"status": 0,"sort": 1,"keyword": "","pageIndex": 1,"pageSize": 15}
        with self.client.post(url, json=data, headers=headers, catch_response=True, name='学习设计查询分页') as response:
            if response.status_code == 200 and 'retcode":0,' in response.text:
                response.success()
                # print('学习设计查询分页成功'+ response.text)
            else:
                response.failure()
                print('学习设计查询分页失败'+ response.text)

    @task
    def catalog(self):
        self.logger = loadLogger(filePath='/Log', fileName='11-13-logs')
        url = 'http://api.forclass.net/Course/api/v1/Asset/catalog'
        headers ={'Authorization':'Bearer '+self.base_session}
        data = {"bookId": 0,"uIdx": 0,"periodId": 0,"subjectId": 0,"editionId": 0,"termId":0}
        with self.client.post(url, json=data, headers=headers, catch_response=True, name='从资源库获取的全部目录结构') as response:
            if response.status_code == 200 and 'retcode":0,' in response.text:
                response.success()
                # print('从资源库获取的全部目录结构成功'+ response.text)
            else:
                response.failure()
                print('从资源库获取的全部目录结构失败'+ response.text)
        self.logger.get_locust_Hook()

class WebsiteUser(FastHttpUser):
    host = 'http://webservice.forclass.net'
    tasks = [MySeqTasks]
    wait_time = between(1, 2)

if __name__ == '__main__':
    import os

    # 启动脚本，以最大请求200个，每秒步进为20
    os.system('locust -f base_271.py --headless -u 1 -r 1')