#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   643. 子数组最大平均数 I.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/2/4 12:06   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例：
输入：[1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75

提示：
1 <= k <= n <= 30,000。
所给数据范围 [-10,000，10,000]。
'''

# import lib
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums or k == 0 or len(nums) == 0:
            return 0
        total = sum(nums[:k])
        total_max = total
        for item_inx in range(k, len(nums)):
            total = total - nums[item_inx - k] + nums[item_inx]
            if total > total_max:
                total_max = total
        return total_max / k


solution = Solution()
# print(solution.findMaxAverage([0, 1, 1, 3, 3], k=4))
print(solution.findMaxAverage([0,4,0,3,2],1))
