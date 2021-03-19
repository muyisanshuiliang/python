#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   705. 设计哈希集合.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/15 10:37   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
不使用任何内建的哈希表库设计一个哈希集合（HashSet）。
实现 MyHashSet 类：
void add(key) 向哈希集合中插入值 key 。
bool contains(key) 返回哈希集合中是否存在这个值 key 。
void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。

示例：
输入：
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
输出：
[null, null, null, true, false, null, true, null, false]
解释：
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // 返回 True
myHashSet.contains(3); // 返回 False ，（未找到）
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // 返回 True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // 返回 False ，（已移除）

提示：
0 <= key <= 106
最多调用 104 次 add、remove 和 contains 。
'''


# import lib
class MyHashSet:

    # 解法一：超大数组
    # 时间复杂度：O(1)
    # 空间复杂度：O(数据范围)
    # def __init__(self):
    #     self.set = [False] * 1000001
    #
    # def add(self, key):
    #     self.set[key] = True
    #
    # def remove(self, key):
    #     self.set[key] = False
    #
    # def contains(self, key):
    #     return self.set[key]

    # 解法二：定长拉链数组
    # 时间复杂度：O(1)
    # 空间复杂度：O(数据范围)
    # def __init__(self):
    #     self.buckets = 1000
    #     self.itemsPerBucket = 1001
    #     self.table = [[] for _ in range(self.buckets)]
    #
    # # 计算桶位置
    # def __hash(self, key):
    #     return key % self.buckets
    #
    # # 计算数据在桶中的位置
    # def __pos(self, key):
    #     return key // self.buckets
    #
    # def add(self, key):
    #     hash_key = self.__hash(key)
    #     if not self.table[hash_key]:
    #         self.table[hash_key] = [0] * self.itemsPerBucket
    #     self.table[hash_key][self.__pos(key)] = 1
    #
    # def remove(self, key):
    #     hash_key = self.__hash(key)
    #     if self.table[hash_key]:
    #         self.table[hash_key][self.__pos(key)] = 0
    #
    # def contains(self, key):
    #     hash_key = self.__hash(key)
    #     return (self.table[hash_key] != []) and (self.table[hash_key][self.__pos(key)] == 1)

    # 解法三：不定长拉链数组
    # 时间复杂度：O(N/b)，N 是元素个数，b 是桶数。
    # 空间复杂度：O(N)
    def __init__(self):
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]

    def __hash(self, key):
        return key % self.buckets

    def add(self, key):
        hash_key = self.__hash(key)
        if key in self.table[hash_key]:
            return
        self.table[hash_key].append(key)

    def remove(self, key):
        hash_key = self.__hash(key)
        if key not in self.table[hash_key]:
            return
        self.table[hash_key].remove(key)

    def contains(self, key):
        hash_key = self.__hash(key)
        return key in self.table[hash_key]

    # 解法四：巧用字典
    # def __init__(self):
    #     """
    #     Initialize your data structure here.
    #     """
    #     self.__data = {}
    #
    # def add(self, key: int) -> None:
    #     self.__data[key] = 1
    #
    # def remove(self, key: int) -> None:
    #     if self.contains(key):
    #         self.__data.pop(key)
    #
    # def contains(self, key: int) -> bool:
    #     """
    #     Returns true if this set contains the specified element
    #     """
    #     if key in self.__data:
    #         return True
    #     return False


hash_set = MyHashSet()
hash_set.add(1)
hash_set.add(2)
print(hash_set.contains(1))
print(hash_set.contains(3))
hash_set.add(2)
print(hash_set.contains(2))
hash_set.remove(2)
print(hash_set.contains(2))