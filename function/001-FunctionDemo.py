print("======================1、默认参数=====================")


# 默认参数值，当第二个参数未传值事，使用默认值
# 必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）
def power(x, n=2):
    n = n - 1
    total = x
    while n > 0:
        total = total * x
        n -= 1
    return total


print(power(5))
print(power(5, 3))


def add_end(L=[]):
    L.append('END')
    return L


def add_end_none(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())
print(add_end())
print(add_end_none())
print(add_end_none())

print("======================2、可变参数=====================")


def cal(numbers):
    sum = 0;
    for item in numbers:
        sum = sum + power(item)
    return sum


def cal_arg(*numbers):
    sum = 0;
    for item in numbers:
        sum = sum + power(item)
    return sum


# 函数调用之前必须先组装成tuple或者list
print(cal([1, 2, 3, 4]))
print(cal((1, 2, 3, 4)))
# TypeError
# print(cal(1, 2, 3, 4))
print(cal_arg(1, 2, 3, 4))
print(cal_arg(1))
# 可变参数，如果是list、tuple，则需要对数据进行拆分
list_number = [1, 2, 3, 4]
print(cal_arg(list_number[0], list_number[1], list_number[2], list_number[3]))
# TypeError
# print(cal_arg((1, 2, 3, 4)))
tuple_number = (1, 2, 3, 4)
print(cal_arg(tuple_number[0], tuple_number[1], tuple_number[2], tuple_number[3]))
# 将元组或者list直接转变成可变参数的最简单方式就是在前面加*
print(cal_arg(*list_number))
print(cal_arg(*tuple_number))

print("======================3、关键字参数=====================")


# 1、关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
# 2、格式：fun(必须参数(arg_name),可选参数(*arg_name),关键字参数(**arg_name))
# 3、限制参数名称的关键字参数格式：fun(必须参数(arg_name),*,关键字参数(arg_name))
#                            fun(必须参数(arg_name),可选参数(*arg_name),关键字参数(arg_name))

def person(name, age, **kw):
    if 'address' in kw:
        print("地址是：%s" % (kw.get("address")))
    print('name:', name, 'age:', age, 'other:', kw)


person("张三", 7)
person("张三", 7, address="成都市")
person("张三", 7, address="成都市", gender="男")

# 从字典中获取参数
extra_dict = {'address': '成都市', 'gender': '男'}
person("张三", 7, address=extra_dict["address"], gender=extra_dict["gender"])
person("张三", 7, **extra_dict)


# 限制关键字参数的名称
def person_arg(name, age, *, address, gender):
    print('name:', name, 'age:', age, 'address:', address, 'gender:', gender)


# def person_arg(name, age, *address, gender):
#     print('name:', name, 'age:', age, 'address:', address, 'gender:', gender)

# TypeError 如果传入了限制参数名称之外的参数，则会报错
# extra_dict = {'address': '成都市', 'gender': '男', 'job': '码农'}
# person_arg("张三", 7, **extra_dict)
extra_dict = {'address': '成都市', 'gender': '男'}
person_arg("张三", 7, **extra_dict)
