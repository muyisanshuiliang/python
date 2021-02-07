#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   665. 非递减数列.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/2/7 9:30   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------
给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。

示例 1:
输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。

示例 2:
输入: nums = [4,2,1]
输出: false
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。

说明：
1 <= n <= 10 ^ 4
- 10 ^ 5 <= nums[i] <= 10 ^ 5
'''

# import lib
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if not nums or len(nums) <= 2:
            return True
        change_number = 0
        # 调整的原则是确保前面的元素尽量小
        for item_inx, item_val in enumerate(nums):
            # 第一个元素不调整
            if item_inx == 0:
                continue
            if item_val < nums[item_inx - 1]:
                # 如果第二个元素的值大于第一个元素的值，将第一个元素的值赋给索引1，确保元素的值尽量小
                if item_inx == 1:
                    nums[item_inx - 1] = nums[item_inx]
                # 后续元素调整，虽然当前元素小于前面的元素，但是大于前面第二个元素，确保元素值尽量小，直接将前面的元素值置为前面的第二个元素
                elif item_val >= nums[item_inx - 2]:
                    nums[item_inx - 1] = nums[item_inx - 2]
                else:
                    # 其余情况都将当前元素值置为前面元素的值
                    nums[item_inx] = nums[item_inx - 1]
                # 修改改变次数
                change_number += 1
            if change_number >= 2:
                break
        # print(nums)
        return change_number <= 1


print(Solution().checkPossibility(nums=[4, 2, 1, 0, -1]))
print(Solution().checkPossibility(nums=[4, 2, 3]))
print(Solution().checkPossibility(nums=[3, 4, 2, 3]))
print(Solution().checkPossibility(nums=[-1, 4, 2, 3]))
