class StudentNoParameter(object):
    pass


class StudentHaveParameter(object):
    # 定义对象的内部私有属性，只需在属性前面添加两个下划线即可
    def __init__(self, name, score, sex):
        self.__name = name
        self.__score = score
        self.__sex = sex

    # 如果需要对对象的内部私有属性进行修改，需要添加相应的getter setter方法
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def get_sex(self):
        return self.__sex

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score

    def set_sex(self, sex):
        self.__sex = sex

    def print_score(self):
        print("%s：%s，%s" % (self.__name, self.__score, self.__sex))

    # 对数据进行格式化
    def print_score_percentage(self):
        print("%s的得分率为：%s" % (self.__name, "{:.2%}".format(self.__score / 100)))

    def print_grade(self):
        print("%s的是%s" % (self.__name, self.get_grade()))

    def get_grade(self):
        if self.__score >= 100:
            return "甲等生"
        elif self.__score >= 80:
            return "乙等生"
        elif self.__score >= 60:
            return "丙等生"
        else:
            return "丁等生"


# 为没有参数的类绑定属性
student = StudentNoParameter()
student.name = "张三"
print(student)
print(student.name)
print(StudentHaveParameter)
print(StudentNoParameter)

parameter = StudentHaveParameter("李四", 95.6, "男生")
print(parameter)
# 调用对象内的函数
parameter.print_score()
parameter.print_score_percentage()
print('percent: {:.2%}'.format(42 / 50))
parameter.print_grade()
# 对类的内部私有属性修改失败
print("=======通过普通方法对内部属性进行修改========")
parameter.__score = 100
parameter.print_score()
parameter.print_grade()
print("=======通过setter方法对内部属性进行修改======")
parameter.set_score(100)
parameter.print_score()
parameter.print_grade()
