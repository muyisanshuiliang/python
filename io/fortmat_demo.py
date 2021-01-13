# 类似于%s的用法，传入的值会按照位置与{}一一对应
str4 = 'my name is {}, my age is {}!'.format('tony', 18)
print(str4)
# my name is tony, my age is 18!

# 把format传入的多个值当作一个列表，然后用{索引}取值
str4 = 'my name is {0}, my age is {1}!'.format('tony', 18)
print(str4)
# my name is tony, my age is 18!

str4 = 'my name is {1}, my age is {0}!'.format('tony', 18)
print(str4)
# my name is 18, my age is tony!

str4 = 'my name is {1}, my age is {1}!'.format('tony', 18)
print(str4)
# my name is 18, my age is 18!

msg = 'tony say hello'
print(msg.index('o', 0, -1))
# print(msg.index('d', 0, -1))

l1 = ['a', 'b', 'c', 'd']
l1.extend(['a', 'b', 'c'])
print(l1)

countries = ("中国", "美国", "英国")
print(type(countries))
countries = ("中国")  # 字符串
print(type(countries))
countries = ("中国",)  # 元组
print(type(countries))

# fromkeys会从元组中取出每个值当做key，然后与None组成key:value放到字典中
dict1 = {}.fromkeys(('name', 'age', 'sex'), None)
print(dict1)
print(dict1.items())

friends1 = {"zero", "kevin", "jason", "egon"}
friends2 = {"Jy", "ricky", "jason", "egon"}
print(friends1 | friends2)
print(friends1 & friends2)
print(friends1 - friends2)
print(friends1 ^ friends2)
