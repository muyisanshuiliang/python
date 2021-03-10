#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   503. 下一个更大元素 II.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/8 16:23   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，
这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

示例 1:
输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数；
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

注意: 输入数组的长度不会超过 10000。
'''

# import lib
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        length = len(nums)
        # 初始化结果集
        res = [-1] * length
        # 单调递减栈
        stack = []
        # 由于是循环数组，依据本题题意，遍历的最大次数为数组2倍
        for i in range(length * 2):
            """
            1、如果单调递减栈不为空：
            2、如果当前索引的数据大于栈顶索引对应的元素
            如果以上两个条件同时满足：说明当前索引的元素即为栈顶元素的下一个更大的元素
            否则将当前数据的索引放入栈中，继续寻找下一个最大的值
            """
            while stack and nums[stack[-1]] < nums[i % length]:
                res[stack.pop()] = nums[i % length]
            stack.append(i % length)
        return res


solution = Solution()
print(solution.nextGreaterElements([1, 2, 1]))
