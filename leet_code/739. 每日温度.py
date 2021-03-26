#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   739. 每日温度.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/24 15:07   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，
请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，
                   你的输出应该是 [1, 1,  4,  2,  1,  1,  0,  0]。
提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。。
'''

# import lib
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        length = len(T)
        res = [0] * length
        # 用于记录单调递增栈的索引
        stack = []
        for item_inx, item_val in enumerate(T):
            # 如果栈不为空或者当前元素的值大于栈顶元素，将栈顶元素弹出，
            # 直到栈空或者栈顶元素大于等于当前元素，不再弹出栈顶元素
            while stack and item_val > T[stack[-1]]:
                pre_index = stack.pop()
                # 索引差值即为该索引所在处值等待的天数
                res[pre_index] = item_inx - pre_index
            # 将当前元素追加到单调递增栈中
            stack.append(item_inx)
        return res


solution = Solution()
print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
