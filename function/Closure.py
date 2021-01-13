def add(x, y):
    return x + y


# 函数可以被引用
function = add
print(function(1, 2))

dic = {'add': add, 'max': max}
print(dic['add'](1, 2))


# 函数可以作为参数传入另外一个函数
def foo(x, y, func):
    return func(x, y)


print(foo(1, 2, function))


# 函数的返回值可以是一个函数
def bar():
    return add


func = bar()
print(func(1, 2))

print("===================闭包测试=========================")
x = 1


def outer():
    x = 2

    def inner():
        print(x)

    return inner

# “闭”代表函数是内部的，“包”代表函数外’包裹’着对外层作用域的引用。因而无论在何处调用闭包函数，使用的仍然是包裹在其外层的变量。
func = outer()
func()
print(func.__closure__)
print(func.__closure__[0].cell_contents)


import requests

#方式一：
def get(url):
    return requests.get(url).text

#方式二：
def page(url):
    def get():
        return requests.get(url).text
    return get

print(get("https://translate.google.cn/?hl=zh-CN#view=home&op=translate&sl=zh-CN&tl=en&text=%E9%97%AD%E5%8C%85"))
python=page('https://translate.google.cn/?hl=zh-CN#view=home&op=translate&sl=zh-CN&tl=en&text=%E9%97%AD%E5%8C%85')
print(python)