# !/usr/bin/python3.6
# -*- coding: UTF-8 -*-
# author: lucien
# 基础包： locust趋势图生成包
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import dates
import matplotlib
matplotlib.use('TkAgg')
hex_colors = [
    '#FF7500',
    '#F00056',
    '#0EB83A',
    '#00BC12',
    '#1BD1A5',
    '#0C8918',
    '#0AA344',
    '#2ADD9C',
    '#3DE1AD',
    '#424C50',
    '#DB5A6B',
    '#FF4E20',
    '#3EEDE7',
    '#4B5CC4',
    '#70F3FF',
    '#2E4E7E',
    '#3B2E7E',
    '#425066',
    '#8D4BBB',
    '#815476',
    '#808080',
    '#161823',
    '#50616D',
    '#725E82',
    '#A78E44',
    '#8C4356',
    '#F47983',
    '#B36D61',
    '#C93756',
    '#FF2121',
    '#C83C23',
    '#9D2933',
    '#FFF143',
    '#FF0097',
    '#A98175',
    '#C32136',
    '#6E511E',
    '#F20C00',
    '#F9906F',
    '#FF8936',
    '#DC3023',
    '#EAFF56',
    '#FFA400',
    '#60281E',
    '#44CEF6',
    '#F0C239',
    '#A88462',
    '#B35C44',
    '#B25D25',
    '#C89B40',
    '#D9B611',
    '#827100',
    '#C3272B',
    '#7C4B00',
    '#BDDD22',
    '#789262',
    '#FF8C31',
    '#C91F37',
    '#00E500',
    '#177CB0',
    '#065279',
]


class data_analyse():
    def __init__(self, filename):
        self.filename = filename
        self.xfmt = dates.DateFormatter('%m/%d %H:%M')
        self._init_graph()  # 初始化趋势图大小
        self._set_graph()  # 初始化趋势图样式

        headers = ['time', 'label',  'method', 'name', 'response_time', 'size']  # 命名字段标题
        self.data = pd.read_csv(filename, sep='|', names=headers)  # 从文件获取内容为DATAFRAME格式
        for col in headers[-2:]:  # 转换response_time和size为int型
            self.data[col] = self.data[col].apply(lambda x: int(x))
        for col in headers[0:-2]:  # 取消掉所有非int型的空格
            self.data[col] = self.data[col].apply(lambda x: x.strip())
        self.data['time'] = self.data['time'].apply(
            lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S,%f'))  # time转化为时间格式
        self.sorted_data = self.data.sort_values(by=['time', 'name'], ascending=[True, True])  # 对数据按照time和name进行降序排列
        self.grouped_data = self.sorted_data.groupby('name')  # 对降序排列的数据，按名称分组
        self.requests_counts = np.array([[key, len(group)] for key, group in self.grouped_data])  # 构建请求名和请求次数数组

    def _init_graph(self):  # 设定趋势图大小
        left, width = 0.1, 0.8
        bottom, height = 0.1, 0.8
        self.trend_scatter = [left, bottom, width, height]

    def _set_graph(self):  # 生成基本趋势图样式
        plt.clf()  # 清除figure中所有axes
        self.ax_plot = plt.axes(self.trend_scatter)  # 套用axes大小
        self.ax_plot.grid(True)  # 打开网格
        self.ax_plot.set_ylabel('Response Time(ms)')  # 纵坐标标题
        self.ax_plot.set_xlabel('time')  # 横坐标标题
        self.ax_plot.figure.set_size_inches(15, 8)  # 画板大小
        self.ax_plot.xaxis.set_major_locator(dates.MinuteLocator(interval=5))  # 设定横坐标日期格式为5min间隔
        self.ax_plot.xaxis.set_major_formatter(self.xfmt)  # 设定横坐标格式

    def generate_trend(self):  # 生成趋势图
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置
        start_index = 0
        legend_list = []
        for index, request in enumerate(self.requests_counts):  # 为数组添加index标签
            name, count = request[0], int(request[1])  # 获取请求名和请求次数
            end_index = start_index + count
            x = self.grouped_data.get_group(name)['time'][start_index: end_index]  # 设置x轴数据
            y = self.grouped_data.get_group(name)['response_time'][start_index:end_index]  # 设置y轴数据
            self.ax_plot.plot(x, y, '-', color=hex_colors[index + 1])  # 画图
            legend_list.append(name)  # 添加请求名到legend中
        plt.legend(legend_list)  # 打印legend
        plt.title(self.filename)
        plt.savefig(fname='.'.join([self.filename, 'png']), dpi=300, bbox_inches='tight')  # 保存趋势图
        plt.show()  # 打印趋势图




if __name__ == '__main__':
    data = data_analyse(r'D:\\Auto\\Log\\test11logs')
    print(data.sorted_data.info())
    data.generate_trend()
