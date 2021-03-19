#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   面试题 03.02. 栈的最小值.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/17 11:06   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
请设计一个栈，除了常规栈支持的pop与push函数以外，还支持min函数，该函数返回栈元素中的最小值。执行push、pop和min操作的时间复杂度必须为O(1)。

示例：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
'''


# import lib
class MinStack:

    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.__data = []
    #     self.__min = []
    #
    # def push(self, x: int) -> None:
    #     self.__data.append(x)
    #     if not self.__min:
    #         self.__min.append(x)
    #     elif self.__min[-1] <= x:
    #         self.__min.append(self.__min[-1])
    #     else:
    #         self.__min.append(x)
    #
    # def pop(self) -> None:
    #     self.__data.pop()
    #     self.__min.pop()
    #
    # def top(self) -> int:
    #     return self.__data[-1]
    #
    # def getMin(self) -> int:
    #     return self.__min[-1]

    def __init__(self):
        self.stack=[]

    def push(self, x: int) -> None:
        min_num = self.stack[-1][1]   if self.stack else  None
        if min_num is None:
            self.stack.append((x,x))
        elif x<=min_num:
            self.stack.append((x,x))
        elif x>min_num:
            self.stack.append((x,min_num))


    def pop(self) -> None:
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1][0]


    def getMin(self) -> int:
         return self.stack[-1][1]
