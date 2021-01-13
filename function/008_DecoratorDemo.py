import time


def timeit(function):
    '''
    第一层函数为装饰器名称
    function：参数，即需要装饰的函数
    return：返回值wrapper，为了保持与原函数参数一致
    '''

    def wrapper(*arg, **args):
        '''
           内层函数，这个函数实现“添加额外功能”的任务
           *arg,**args：参数保持与需要装饰的函数参数一致，这里用*arg和**args代替
        '''
        start = int(time.time() * 1000)
        # 这里就是额外功能代码
        function()  # 执行原函数
        # 这里就是额外功能代码
        end = int(time.time() * 1000)
        print(f'函数执行所花费的时间为：{end - start}')

    return wrapper


def method_decoration(function):  # 外层decorator
    c = 150
    d = 200

    def wrapper(a, b):  # 内层wrapper。和add_function参数要一样
        # wrapper需要保证与add_function参数一致。因为返回的wrapper就是add_function，所以要统一，我们可以使用*arg,和**args去匹配任何参数；
        result = function(a, b)
        result = result * c / d  # 加密，相当于添加额外功能
        # wrapper一定要返回值。因为add_function函数是需要返回值的。
        return result  # 此处一定要返回值

    return wrapper


@method_decoration
def add_function(a, b):
    return a + b


result = add_function(100, 300)  # 函数调用
print(result)


@timeit
def my_function():
    print("我是 my_function 函数")
    # time.sleep(10)


my_function()

