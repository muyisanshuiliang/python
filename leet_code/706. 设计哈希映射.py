#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   706. 设计哈希映射.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/15 11:13   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
不使用任何内建的哈希表库设计一个哈希映射（HashMap）。
实现 MyHashMap 类：
MyHashMap() 用空映射初始化对象
void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。

示例：
输入：
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
输出：
[null, null, null, 1, -1, null, 1, null, -1]
解释：
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // myHashMap 现在为 [[1,1]]
myHashMap.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]]
myHashMap.get(1);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]]
myHashMap.get(3);    // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]]
myHashMap.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值）
myHashMap.get(2);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]]
myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]]
myHashMap.get(2);    // 返回 -1（未找到），myHashMap 现在为 [[1,1]]

提示：
0 <= key, value <= 106
最多调用 104 次 put、get 和 remove 方法
进阶：你能否不使用内置的 HashMap 库解决此问题？
'''


# import lib
class MyHashMap:

    # 解法一：超大数组
    # 时间复杂度：O(1)
    # 空间复杂度：O(数据范围)
    # def __init__(self):
    #     """
    #     Initialize your data structure here.
    #     """
    #     self.__data = [-1] * 1000001
    #
    # def put(self, key: int, value: int) -> None:
    #     """
    #     value will always be non-negative.
    #     """
    #     self.__data[key] = value
    #
    # def get(self, key: int) -> int:
    #     """
    #     Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
    #     """
    #     return self.__data[key]
    #
    # def remove(self, key: int) -> None:
    #     """
    #     Removes the mapping of the specified value key if this map contains a mapping for the key
    #     """
    #     self.__data[key] = -1

    # 解法二：定长数组拉链法
    # 时间复杂度：O(1)
    # 空间复杂度：O(数据范围)
    # def __init__(self):
    #     self.map = [[-1] * 1000 for _ in range(1001)]
    #
    # def put(self, key, value):
    #     # 确定数据的具体位置
    #     row, col = key // 1000, key % 1000
    #     self.map[row][col] = value
    #
    # def get(self, key):
    #     row, col = key // 1000, key % 1000
    #     return self.map[row][col]
    #
    # def remove(self, key):
    #     row, col = key // 1000, key % 1000
    #     self.map[row][col] = -1

    # 解法三：不定长数组拉链法
    # 时间复杂度：$$O(N/b)$$，N 是元素个数，b 是桶数。
    # 空间复杂度：$$O(N)$$
    def __init__(self):
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]

    def __hash(self, key):
        return key % self.buckets

    def put(self, key: int, value: int) -> None:
        # 计算桶位置
        hash_key = self.__hash(key)
        # 遍历该桶内的元素，
        for item in self.table[hash_key]:
            # 桶内元素是一个长度为2的列表，[key,value],如果找到key，则更新对应的value
            if item[0] == key:
                item[1] = value
                return
        # 如果桶内元素没有，则追加这个新值
        self.table[hash_key].append([key, value])

    def get(self, key: int) -> int:
        hash_key = self.__hash(key)
        for item in self.table[hash_key]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        hash_key = self.__hash(key)
        for i, item in enumerate(self.table[hash_key]):
            if item[0] == key:
                self.table[hash_key].pop(i)
                return


hash_map = MyHashMap()
hash_map.put(15, 23)
print(hash_map)
hash_map.put(1024, 23)
hash_map.put(2033,56)
print(hash_map)