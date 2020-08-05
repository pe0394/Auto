from locust import HttpUser, TaskSet, task, between,SequentialTaskSet
import csv
import json
import queue    #导入队列
from locust.contrib.fasthttp import FastHttpUser    #异步请求,不考虑服务端返回的数据

class MySeqTasks(SequentialTaskSet):
#class MyTaskSet(TaskSet):
    logindata = queue.Queue()  # 队列实例化
    csvFile = open(r'D:\\Auto\\test\\anhui_test_fu.csv', 'r')  # 读取本地csv，只读模式
    reader = csv.reader(csvFile)
    for row in reader:  # 循环遍历将表内账号密码放入logindata
        logindata.put({"account": row[0], "password": row[1], "page": "0"})
    logindata.task_done()
    @task
    def LoginAccountJson(self):
    # def on_start(self):

        url = '/AccountService.asmx/LoginAccountJson'
        headers = {'Host': 'test.ws.forclass.net'}
        try:
            body = self.logindata.get()  # 获取队列里的数据
        except queue.Empty:     #队列取空后，直接退出
            exit(0)
        with self.client.post(url, headers=headers, data=body,  timeout=120, catch_response=True, name='登录') as response:
            if response.status_code == 200 and response.json()['ReturnCode'] == 1:
                response.success()
                print('登录成功', response.text)
            else:
                print(response.text, '登录失败')
                print(body['account'])
                response.failure('LoginAccountJson_ 接口失败！')
                file_handle = open('1.txt', mode='a')
                file_handle.write(str(body['account']) + '\n')
                file_handle.close()


class WebsiteUser(FastHttpUser):
    host = 'http://test.zzn.forclass.net'
    tasks = [MySeqTasks]
    wait_time = between(0.1, 0.2)   # 设置请求的思考时间范围,单位是秒


if __name__ == '__main__':
    import os

    # 启动脚本，以最大请求200个，每秒步进为20
    os.system('locust -f locust_paas.py --headless -u 200 -r 20')
