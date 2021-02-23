#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   908. 最小差值 I.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/2/23 17:03   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------
给你一个整数数组 A，请你给数组中的每个元素 A[i] 都加上一个任意数字 x （-K <= x <= K），从而得到一个新数组 B 。
返回数组 B 的最大值和最小值之间可能存在的最小差值。

示例 1：
输入：A = [1], K = 0
输出：0
解释：B = [1]

示例 2：
输入：A = [0,10], K = 2
输出：6
解释：B = [2,8]

示例 3：
输入：A = [1,3,6], K = 3
输出：0
解释：B = [3,3,3] 或 B = [4,4,4]
 

提示：
1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000

'''

# import lib
from typing import List


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        # 与中位数进行比较
        # max_val = max(A)
        # min_val = min(A)
        # mid_val = (min_val + max_val) // 2
        # if min_val + K >= mid_val:
        #     return 0
        # else:
        #     return max_val - min_val - 2 * K

        #
        # return max(max(A) - min(A) - 2*K, 0)

        a = max(A) - K
        b = min(A) + K
        if b >= a:
            return 0
        else:
            return a - b


solution = Solution()
print(solution.smallestRangeI(A=[1, 3, 6], K=3))
