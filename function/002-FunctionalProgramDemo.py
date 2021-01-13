from functools import reduce

print("===============函数式编程===============")

print("===============1、map函数===============")


def power(x):
    return x * x


# map()传入的第一个参数是f，即函数对象本身
list_number = [1, 2, 3, 4, 5]
# 结果iterator是一个Iterator，Iterator是惰性序列
iterator = map(power, list_number)
# 通过list()函数让它把整个序列都计算出来并返回一个list
list_number = list(iterator)
print(list_number)

# 将列表的所有元素转换成string
print(list(map(str, list_number)))

print("===============2、reduce函数===============")


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算


def add(a, b):
    return a + b


def append(a, b):
    if not isinstance(a, str):
        a = str(a)
    if not isinstance(b, str):
        b = str(b)
    return a + b


def total(a, b):
    return a * 10 + b


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


list_number = [1, 2, 3, 4, 5]
number = reduce(add, list_number)
print(number)

print(reduce(append, list_number))
print(reduce(total, list_number))
# 字符串转数字
print(reduce(total, map(char2num, "13579")))

print("===============3、filter函数===============")

# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
from math import sqrt


def odd(c):
    return c % 2 == 1


def all_in_prime(n):
    prime_number = []
    if n == 1:
        return prime_number
    else:
        list_number = list(range(2, n))
        list_number.append(n)
        prime_number = list(filter(is_prime, list_number))
    return prime_number


def is_prime(n):
    # 素数的概念：大于1，只能被自身和1整除的数据为素数
    max = int(sqrt(n)) + 1
    for x in range(2, max):
        if n % x == 0:
            return False
    return True


print(list(range(2, 2)))
list_number = [1, 2, 3, 4, 5]
# 返回的是一个Iterator，Iterator是惰性序列，需要通过list把整个序列都计算出来并返回一个list
print(list(filter(odd, list_number)))

print("%s 以内的素数：%s" % (11, all_in_prime(11)))

print("===============3、sorted函数===============")
# 默认升序，可以通过 reverse=True 控制排序方式为降序
print(sorted([36, 5, -12, 9, -21], reverse=True))
print(sorted([36, 5, -12, 9, -21]))

# 可以自定义函数进行排序,如下按照绝对值进行排序
print(sorted([36, 5, -12, 9, -21], key=abs))
print(sorted([36, 5, -12, 9, -21], key=abs, reverse=True))

# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
print("正常排序 %s" % sorted(['bob', 'about', 'Zoo', 'Credit']))
print("逆序排序 %s" % sorted(['bob', 'about', 'Zoo', 'Credit'], reverse=True))
print("忽略大小写 %s" % sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))


def sortedDictValues1(adict):
    keys = adict.keys()
    # l = sorted(keys)
    return [value for key, value in keys]


# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L = {'Bob': 75, 'Adam': 92, 'Bart': 66, 'Lisa': 88}
# print(sortedDictValues1(L))
print("通过key进行升序：%s" % sorted(L.items(), key=lambda item: item[0]))
print("通过value进行升序：%s" % sorted(L.items(), key=lambda item: item[1]))
print("通过key进行降序：%s" % sorted(L.items(), key=lambda item: item[0], reverse=True))
print("通过value进行降序：%s" % sorted(L.items(), key=lambda item: item[1], reverse=True))

print("===============4、函数作为返回值===============")


# 在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


list_number = [1, 2, 3, 4, 5]
function = lazy_sum(*list_number)
print("function的类型：%s" % type(function))
print("调用function = %s" % function())
# 每次调用都会返回一个新的函数，即使传入相同的参数
another_function = lazy_sum(*list_number)
print(function == another_function)

print("===============5、装饰器===============")


# 在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
def now():
    print('2020-04-21')


function = now
print("函数名称：%s" % function.__name__)
print("函数名称：%s" % now.__name__)

# 调用function函数
function()


# 函数作为一个参数进行传递
def print_now(fun):
    fun()


# 调用函数
print_now(now)
