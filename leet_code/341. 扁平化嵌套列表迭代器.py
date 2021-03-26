#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   341. 扁平化嵌套列表迭代器.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/23 9:42   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。
列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。

示例 1:
输入: [[1,1],2,[1,1]]
输出: [1,1,2,1,1]
解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。

示例 2:
输入: [1,[4,[6]]]
输出: [1,4,6]
解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。
'''

# import lib
import collections


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:

    # 解法一：递归初始化元素，全部展平，放到一个列表中
    # def dfs(self, nests):
    #     for nest in nests:
    #         if nest.isInteger():
    #             self.queue.append(nest.getInteger())
    #         else:
    #             self.dfs(nest.getList())
    #
    # def __init__(self, nestedList):
    #     self.queue = collections.deque()
    #     self.dfs(nestedList)
    #
    # def next(self):
    #     return self.queue.popleft()
    #
    # def hasNext(self):
    #     return len(self.queue)

    # 解法二：一边迭代一边获取当前的结果
    def __init__(self, nestedList):
        self.stack = []
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])

    def next(self):
        cur = self.stack.pop()
        return cur.getInteger()

    def hasNext(self):
        # 如果栈不为空
        while self.stack:
            # 获取栈顶的第一个元素
            cur = self.stack[-1]
            # 如果栈顶的原始是数字直接返回True
            if cur.isInteger():
                return True
            # 如果栈顶的第一个元素不是数字，取出栈顶的元素，
            self.stack.pop()
            # 将该元素依次展平，原则 先进后出
            for i in range(len(cur.getList()) - 1, -1, -1):
                self.stack.append(cur.getList()[i])
        return False
