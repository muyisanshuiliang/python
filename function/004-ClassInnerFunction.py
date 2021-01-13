print("=====================Class内部的方法=======================")


class Student:
    """学生信息"""

    # 定义对象的内部私有属性，只需在属性前面添加两个下划线即可
    def __init__(self, name, score, sex):
        """学生名称"""
        self.__name = name
        """学生分数"""
        self.__score = score
        """学生性别"""
        self.__sex = sex

    # def __del__(self):
    #     print("%s 对象被回收了" % self)

    def __call__(self, *args, **kwargs):
        print('__call__')

    def __str__(self):
        return '[name = {0},score = {1},sex = {2}]'.format(self.__name,self.__score,self.__sex)

    def __setitem__(self, key, value):
        key = value
        print(self)




# 1、__doc__：说明性文档和信息
print("%s" % Student.__doc__)
# 2、__init__：实例化方法，通过类创建实例时，自动触发执行
obj = Student('张三', 95, '男')
# 3、__module__：表示当前操作的对象在属于哪个模块
print(obj.__module__)
# 4、__class__：表示当前操作的对象属于哪个类
print(obj.__class__)
# 5、__del__()：析构方法，当对象在内存中被释放时，需要在释放的时候指定做一些动作。析构函数的调用是由解释器在进行垃圾回收时自动触发执行的。
# del obj
# 6、__call__()：如果为一个类编写了该方法，那么在该类的实例后面加括号，
# 可会调用这个方法，构造方法的执行是由类加括号执行的，即：对象 = 类名()，而对于__call__() 方法，是由对象后加括号触发的，即：对象() 或者 类()()
# 可以用Python内建的callable()函数进行测试对象是否一个Callable对象
if callable(obj):
    obj()
else:
    print("对象不能被执行")
# 7、__dict__()：获取类的成员
print(Student.__dict__)
# 获取对象的成员
print(obj.__dict__)

# 8、__str__()：如果一个类中定义了__str__()方法，那么在打印对象时，默认输出该方法的返回值。这也是一个非常重要的方法，需要用户自己定义。　
# 下面的类，没有定义__str__()方法，打印结果是：<__main__.Foo object at 0x000000000210A358>
print(obj)

obj.__setitem__('name',"修改后的值")