#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 30. 包含min函数的栈.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/15 16:27   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
 
提示：
各函数的调用总次数不超过 20000 次
'''


# import lib
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__data = []
        self.__min_data = []

    def push(self, x: int) -> None:
        self.__data.append(x)
        if self.__min_data.__len__() == 0:
            self.__min_data.append(x)
        else:
            self.__min_data.append(x if x < self.__min_data[-1] else self.__min_data[-1])

    def pop(self) -> None:
        if len(self.__data) == 0:
            return None
        self.__data.pop()
        self.__min_data.pop()

    def top(self) -> int:
        if len(self.__data) == 0:
            return None
        return self.__data[-1]

    def min(self) -> int:
        if self.__min_data.__len__() == 0:
            return None
        return self.__min_data[-1]
