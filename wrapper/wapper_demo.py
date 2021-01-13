import time

print(time.time())


def timer1(func):# func = wrapper2的内存地址
    def wrapper1(*args, **kwargs):
        print("正在运行timer1 =====> ")
        start_time = time.time()
        res = func(*args, **kwargs)
        time.sleep(3)
        stop_time = time.time()
        print("%s function execution taste %d sec" % (func.__name__, stop_time - start_time))
        return res
    return wrapper1


def timer2(func):# func = wrapper3的内存地址
    def wrapper2(*args, **kwargs):
        print("正在运行timer2 =====> ")
        start_time = time.time()
        res = func(*args, **kwargs)
        time.sleep(3)
        stop_time = time.time()
        print("%s function execution taste %d sec" % (func.__name__, stop_time - start_time))
        return res

    return wrapper2


def timer3(msg):
    def inner_timer(func): # func = say_hello的内存地址
        def wrapper3(*args, **kwargs):
            print("正在运行timer3 =====> %s " % msg)
            start_time = time.time()
            res = func(*args, **kwargs)
            time.sleep(3)
            stop_time = time.time()
            print("%s function execution taste %d sec" % (func.__name__, stop_time - start_time))
            return res
        return wrapper3
    return inner_timer

# 自下而上加载，自上而下运行
@timer1
@timer2
@timer3(msg="我是第三个时间测试")
def say_hello(value):
    print("Hello,%s!" % value)


say_hello("python")
