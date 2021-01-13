print("=====================字典的常用操作=======================")
# L1 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = {'Bob': 75, 'Adam': 92, 'Bart': 66, 'Lisa': 88}

print("=====================1、遍历KEY=======================")

for key in L2:
    print("第一种 %s" % key)

for key in L2.keys():
    print("第二种 %s" % key)

# for key in L2.iterkeys():
#     print("第三种 %s" % key)

print(dir(L2))

print("=====================2、遍历VALUE=======================")
for value in L2.values():
    print("第一种 %s" % value)

print("=====================3、遍历KEY和VALUE=======================")

print("========方法一：通过遍历key来进行遍历=========")
for item in L2:
    print("L2[%s]=" % item, L2[item])

print("========方法二：直接遍历=========")
for item in L2.items():
    print(item)

print("========方法三：key,value遍历=========")
for (k, v) in L2.items():
    print("L2[%s]=" % k, v)

print("=====================4、字典转LIST=======================")
# key转List
print(list(L2))
# 键值对转List
print(list(L2.items()))
# List转字典
print(dict(list(L2.items())))
