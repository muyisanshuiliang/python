# with open('db1.txt', mode='r', encoding='utf-8') as f:
#     readlines = f.readlines(1)
#     print(readlines)

# readline = f.readline()
# print(readline)

# read = f.read()
# print(read)

# 之前文件内指针的移动都是由读/写操作而被动触发的，若想读取文件某一特定位置的数据，则则需要用f.seek方法主动控制文件内指针的移动，详细用法如下：
# f.seek(指针移动的字节数,模式控制):
# 模式控制:
# 0: 默认的模式,该模式代表指针移动的字节数是以文件开头为参照的
# 1: 该模式代表指针移动的字节数是以当前所在的位置为参照的
# 2: 该模式代表指针移动的字节数是以文件末尾的位置为参照的
# 强调:其中0模式可以在t或者b模式使用,而1跟2模式只能在b模式下用

# 0模式的使用
with open('db1.txt', mode='rt', encoding='utf-8') as f:
    f.seek(3, 0)  # 参照文件开头移动了3个字节
    print(f.tell())  # 查看当前文件指针距离文件开头的位置，输出结果为3
    print(f.read())  # 从第3个字节的位置读到文件末尾，输出结果为：ngsan:123456
    # 注意：由于在t模式下，会将读取的内容自动解码，所以必须保证读取的内容是一个完整中文数据，否则解码失败

# with open('a.txt',mode='rb') as f:
#     f.seek(6,0)
#     print(f.read().decode('utf-8')) #输出结果为: 好
