#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1295. 统计位数为偶数的数字.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/12 12:27   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
给你一个整数数组 nums，请你返回其中位数为 偶数 的数字的个数。

示例 1：
输入：nums = [12,345,2,6,7896]
输出：2
解释：
12 是 2 位数字（位数为偶数）
345 是 3 位数字（位数为奇数）
2 是 1 位数字（位数为奇数）
6 是 1 位数字 位数为奇数）
7896 是 4 位数字（位数为偶数）
因此只有 12 和 7896 是位数为偶数的数字

示例 2：
输入：nums = [555,901,482,1771]
输出：1
解释：
只有 1771 是位数为偶数的数字。

提示：
1 <= nums.length <= 500
1 <= nums[i] <= 10^5
'''

# import lib
import math
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # return sum(1 for item in nums if (len(str(item)) % 2 == 0))

        return sum(1 for num in nums if int(math.log10(num) + 1) % 2 == 0)

