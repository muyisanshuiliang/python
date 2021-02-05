"""
般来说，itertools模块包含创建有效迭代器的函数，可以用各种方式对数据进行循环操作，
此模块中的所有函数返回的迭代器都可以与for循环语句以及其他包含迭代器（如生成器和生成器表达式）的函数联合使用。
"""
from itertools import chain, combinations, count

chain_data = chain('1', '2', [3, 4, 5], (7, 8, 9), {1: 'a', 2: 'b'})
# for item in chain_data:
#     print(type(item))
#     print(item)

# 一个备用链构造函数
test = chain.from_iterable('ABCDEF')
print(test.__next__())
print(test.__next__())
print(test.__next__())
print(test.__next__())

# 创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序:
test = combinations([1,2,3,4], 2)
print(list(test))
test = combinations([1,2,3,4], 3)
print(list(test))

test = count([10])
print(list(test))
