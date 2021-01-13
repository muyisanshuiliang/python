def foo():
    print('in the foo')
    bar()


def bar():
    print('in the bar')


def double(x, y, z):
    return x * 2, y * 2, z * 2
    # 多个return，只执行第一个
    return 'hello'


foo()
double_value = double("yl", 234, "234")
print(type(double_value))
print(double_value)
