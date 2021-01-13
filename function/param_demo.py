# 函数的参数分为形式参数和实际参数，简称形参和实参：
#
# 形参即在定义函数时，括号内声明的参数。形参本质就是一个变量名，用来接收外部传来的值。
#
# 实参即在调用函数时，括号内传入的值，值可以是常量、变量、表达式或三者的组合:
# 定义位置形参：name，age，sex，三者都必须被传值，school有默认值
def register(name, age, sex, school='Tsinghua'):
    print('Name:%s Age:%s Sex:%s School:%s' % (name, age, sex, school))


def foo(x, y, z=3, *args):
    print(x)
    print(y)
    print(z)
    print(args)
    return


def foo1(x, y, z=3, **args):
    print(x)
    print(y)
    print(z)
    print(args)
    return


# 用*作为一个分隔符号，号之后的形参称为命名关键字参数。对于这类参数，在函数调用时，必须按照key=value的形式为其传值，且必须被传值
# 另外，如果形参中已经有一个args了，命名关键字参数就不再需要一个单独的*作为分隔符号了
def register1(name, age, *args, sex='male', height):
    # def register1(name, age, *, sex, height):
    print('Name:%s Age:%s Sex:%s Height:%s Other:%s' % (name, age, sex, height, args))


x = 1


def outer():
    # 若要在函数内修改全局名称空间中名字的值，当值为不可变类型时，则需要用到global关键字
    # global x
    x = 2
    def inner():  # 函数名inner属于outer这一层作用域的名字
        # 对于嵌套多层的函数，使用nonlocal关键字可以将名字声明为来自外部嵌套函数定义的作用域（非全局）
        nonlocal x
        x = 3
        print('inner x:%s' % x)

    inner()
    print('outer x:%s' % x)


print("全局变量修改前 x = %d" % x)
outer()
print("全局变量修改后 x = %d" % x)



# register()  # TypeError：缺少3个位置参数
# register(sex='male', name='lili', age=18)
# register('lili', sex='male', age=18, school="Peking University")  # 正确使用
# 实参也可以是按位置或按关键字的混合使用，但必须保证关键字参数在位置参数后面，且不可以对一个形参重复赋值
# register(name='lili',18,sex='male') #SyntaxError: positional argument follows keyword argument：关键字参数name=‘lili’在位置参数18之前
# register('lili',sex='male',age=18,name='jack') #TypeError: register() got multiple values for argument 'name'：形参name被重复赋值

# foo(1, 2, 3, 4, 5, 6, 7)
# L = [3, 4, 5]
# foo(1, 2, *L)
# foo(1, 2, L)
# dic = {'a': 1, 'b': 2}
# foo1(1, 2, **dic)

# register1('lili', 18, height='1.8m')
