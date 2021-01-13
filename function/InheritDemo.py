from types import MethodType


class People(object):

    def run(self):
        print("我是父类的方法")


# 子类如果有该方法，则调用子类方法，没有则直接调用父类方法
class Student(People):
    def run(self):
        print("我是一个学生")


class Worker(People):
    name = "张三"

    def eat(self):
        print("工人需要吃肉")


def run_twice(people):
    people.run()
    people.run()


student = Student()
student.run()
worker = Worker()
worker.run()

run_twice(student)
run_twice(worker)
# 判断一个变量是否是某个类型可以用isinstance()判断：
if isinstance(student, Student):
    print("student 是学生")
else:
    print("student不是学生")

if isinstance(worker, People):
    print("worker 是人")
else:
    print("worker 不是人")

# 获取一个数据的类型
print("student的类型 %s" % (type(student)))
print(type(Student))

print("类的属性：%s" % Worker.name)
print("实例的属性：%s" % worker.name)
# 修改的是类属性值
Worker.name = "李四"
print("类的属性：%s" % Worker.name)
print("实例的属性：%s" % worker.name)
# 修改的是实例属性值
worker.name = "王五"
print("类的属性：%s" % Worker.name)
print("实例的属性：%s" % worker.name)

print("============实例绑定方法================")


# 为实例绑定方法，self参数不可缺少
def print_work_instance(self, workName):
    print("我是一个 %s 工人" % workName)


worker.print_work = MethodType(print_work_instance, worker)
worker.print_work("木匠")

print("==========类的属性和方法绑定方式============")


# 为类例绑定方法，self参数不可缺少
def print_work_class_first(self):
    print("我是类的第一种绑定方法")


def print_work_class_second(self):
    print("我是类的第二种绑定方法")


# 第一种方式
Worker.print_work_class_first = MethodType(print_work_class_first, Worker)
newWork = Worker()
newWork.print_work_class_first()
# 第一种方式
Worker.print_work_class_second = print_work_class_second
anotherWorker = Worker()
anotherWorker.print_work_class_second()

print("========限制类属性的名称==========")


class Animal(object):
    # 限制只能对name、age进行修改
    __slots__ = ('name', 'age')
    pass


dog = Animal()
dog.name = "张川西"
dog.age = 100
print("我家小狗的名字是%s，年龄是%s" % (dog.name, dog.age))
