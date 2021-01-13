# 1、得分定义有名函数
# func = 函数的内存地址
# def func(x, y):
#     return x + y


# 2、lambda 定义匿名函数
from functools import reduce

lambda x, y: x + y

# 3、匿名函数的调用
# 方式一：
res = (lambda x, y: x + y)(1, 2)
print(res)

# 方式二：内存地址赋值，闲的蛋疼的操作
func = lambda x, y: x + y
print(func)
res = func(1, 2)
print(res)

# 方式三：匿名函数与有名函数的最大区别就是，临时调用一次，更多的是将匿名函数与其他函数配合使用
salaries = {"ell": 2500, "tom": 1500, "lily": 3500, "lucy": 4500}

# max函数在没有指定比较key(比较的依据)的情况下，会一次比较从迭代器中取出的值
res = max(salaries)
print(res)


# 字典迭代出来的值是key,但是需要根据value来进行比较标准
def get_value(key):
    return salaries[key]


# 这里key直接指向一个函数，会自动将迭代出来的值传递到这个函数中
res = max(salaries, key=get_value)
print(res)

res = max(salaries, key=lambda item: salaries[item])
print(res)
#  min函数与max类似

res = sorted(salaries)
print(res)
res = sorted(salaries, key=lambda item: salaries[item])
print(res)
res = sorted(salaries, key=lambda item: salaries[item], reverse=True)
print(res)

res = map(lambda item: item + "_dsb", salaries)
iterator = res.__iter__()

while True:
    try:
        key = next(iterator)
        print(key)
    except StopIteration:
        break

# filter reduce

res = reduce(lambda x, y: x + y, [1, 2, 3, 4], 10)
print(res)
