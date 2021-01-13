import os

with open("test.doc", "w") as f:
    for item in range(1, 100, 3):
        f.write(str(item) + "\n")
    # with模块执行完毕后，会自动关闭文件
    # f.close()

with open("test.doc", "w") as f:
    for item in range(1, 100, 2):
        if (item % 3) == 0:
            f.write("我是第 %s 个数字。\n" % item)

# 获取系统的环境变量
with open("environment.doc", "w") as f:
    f.write("系统的环境变量\n")
    environs = os.environ
    for item in environs:
        f.write("name = %s ,valve = %s \n" % (item, environs.get(item)))

# 如果不关闭文件，那么会从读到的位置开始读取数据，并不会从开始读取
f = open("test.doc")
# 读取文件内容， size为读取的长度，以byte为单位
print(f.read(12))
# 如果定义了size，有可能返回的只是一行的一部分
print(f.readline(6))
f.close()


def read_file(fileName):
    with open(fileName, "r") as f:
        # 把文件每一行作为一个list的一个成员，并返回这个list。其实它的内部是通过循环调用readline()来实现的。
        # 如果提供size参数，size是表示读取内容的总长，也就是说可能只读到文件的一部分
        list = f.readlines()
        i = 1
        for item in list:
            if isinstance(item, str):
                item = item.replace("\n", "")
                print("第 %s 行数据：%s" % (i, item))
                i += 1


read_file("environment.doc")
