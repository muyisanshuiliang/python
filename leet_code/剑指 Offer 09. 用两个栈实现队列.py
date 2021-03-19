#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 09. 用两个栈实现队列.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/17 11:11   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]

示例 2：
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]

提示：
1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用
'''

# import lib
class CQueue:

    # def __init__(self):
    #     self.__data = []
    #
    #
    # def appendTail(self, value: int) -> None:
    #     self.__data.append(value)
    #
    #
    # def deleteHead(self) -> int:
    #     if not self.__data:
    #         return -1
    #     return self.__data.pop(0)

    def __init__(self):
        self.a, self.b = [], []

    def appendTail(self, value: int) -> None:
        self.a.append(value)

    def deleteHead(self) -> int:
        if self.b:
            return self.b.pop()
        if not self.a:
            return -1
        # 先入的先出
        while self.a:
            self.b.append(self.a.pop())
        return self.b.pop()