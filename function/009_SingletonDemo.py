class Student(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Student, cls).__new__(cls)
        return cls.instance

    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student('张三', 23)
s2 = Student('李四', 24)
print((s1 == s2))
print(s1 is s2)
print(id(s1), id(s2), sep='   ')
