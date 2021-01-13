# 关于print函数的使用
import time


def print_sharp(n):
    item = 0
    while item < n:
        print("#")
        item += 1


# print 函数中的 end 默认是 \n
print_sharp(10)


# 通过修改end值，改变打印是否换行，
# 虽然是一行，不过它是整块一起出来的
def print_sharp_end(n):
    item = 0
    while item < n:
        print("#", end='')
        item += 1


print_sharp_end(10)

print("\n")


# flush 默认为 False,只有所有内容都有了，然后一次性都打印出来
# 而使用 True 就可以做到，每次打印都及时显示出来，使用 sleep 来看看显示效果
def print_sharp_flush(n):
    item = 0
    while item < n:
        print("#", end='', flush=True)
        item += 1
        time.sleep(1)


# print_sharp_flush(10)

print('\n')


# \r 这个转义字符，它可以做到每次都回到开头
def print_sharp_percent(n):
    item = 1
    while item < n:
        print('\r', '进度百分比：{0}%。'.format(round(item) * 100 / n), end='', flush=True)
        item += 1
        time.sleep(1)

    # print_sharp_percent(100)
