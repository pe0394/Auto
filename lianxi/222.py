from lianxi import csv

file = open(r'D:\test.csv')
datas = csv.reader(file)
list = []
for data in datas:
    if data == 0:
        pass
    else:
        list.append(data)


# for index in range(1,10,2):
#     print(list[index])
#     print(list[index][0])
#     print(list[index][1])
#     print(list[index][2])


for w in list:
    if w[0] in "login":
        pass
    else:
        print(w[0]+ ' ' + w[1])