#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   456. 132模式.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/16 10:55   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < aj。设计一个算法，当给定有 n 个数字的序列时，
验证这个序列中是否含有132模式的子序列。
注意：n 的值小于15000。

示例1:
输入: [1, 2, 3, 4]
输出: False
解释: 序列中不存在132模式的子序列。

示例 2:
输入: [3, 1, 4, 2]
输出: True
解释: 序列中有 1 个132模式的子序列： [1, 4, 2].

示例 3:
输入: [-1, 3, 2, 0]
输出: True
解释: 序列中有 3 个132模式的的子序列: [-1, 3, 2], [-1, 3, 0] 和 [-1, 2, 0].
'''

# import lib
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if not nums or len(nums) <= 2:
            return False
        le = len(nums)
        # 维护一个最小值的数组，该数组的值对应的是该索引下已知的最小值
        mi = [nums[0]]
        for i in range(1, le):
            mi.append(min(nums[i], mi[-1]))
        print(mi)
        # 单调栈
        stack = []
        for i in range(le - 1, -1, -1):
            print(stack)
            # 如果当前值小于最小值，不符合132模式，直接抛弃当前数据
            if nums[i] > mi[i]:
                # 如果单调栈不为空，并且小于当前索引对应的最小值，说明该值是不符合要求的，直接弹出该元素
                while stack and mi[i] >= stack[-1]:
                    stack.pop()
                # 如果单调栈不为空，且单调栈的元素小于当前值，符合132模式，返回
                if stack and stack[-1] < nums[i]:
                    return True
                # 将当前元素追加到单调栈中
                stack.append(nums[i])
        return False

        # if not nums or len(nums) <= 2:
        #     return False
        # le = len(nums)
        # # 维护一个最小值的数组，该数组的值对应的是该索引下已知的最小值
        # mi = [nums[0]]
        # for i in range(1, le):
        #     mi.append(min(nums[i], mi[-1]))
        # print(mi)
        # # 循环判断后面的额元素是否满足题意需求，提交会超时
        # for i in range(le - 1, -1, -1):
        #     temp_inx = i + 1
        #     while temp_inx < le:
        #         if mi[i] < nums[temp_inx] < nums[i]:
        #             return True
        #         temp_inx += 1
        # return False


solution = Solution()
print(solution.find132pattern([1, 0, 1, -4, -3]))
