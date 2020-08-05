from lianxi import csv

file = open(r'D:\test.csv')
datas = csv.reader(file)#读取csv中的数据，给datas变量
list = [] #全局声明一个空的数组
for data in datas:  #遍历datas中的行
    if data == 0:   #如果某行数据为空，则不添加到list中，直接pass
        pass
    else:           #如果数据不为空，则将数据转换为元组tuple，然后添加到list中
        tb = tuple(data)    #data转换为元组tuple
        list.append(tb)     #元组tuple添加到列表list变量中
for ls in list:             #遍历list中的每一个元组tuple，进行打印
    if ls[0] == 'login':    #如果第一行第一列有login，直接pass不打印
        pass
    else:
        print('账号：'+ls[0] +' 密码：'+ls[1])    #元组中下标为0的是账号，下标为1的是密码

#给我第二个账号密码
print('第二个账号：'+list[1][0] +'第二个密码：'+list[1][1])
