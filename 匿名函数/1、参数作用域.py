def change():
    # print("函数接收到的参数：%d", a)
    global a
    a = 100
    print("函数修改值后的参数：%d" % (a))


a = 10
change()
print("修改后的值：%d" % a)
