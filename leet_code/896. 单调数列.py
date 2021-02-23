#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   896. 单调数列.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/2/23 17:12   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------
如果数组是单调递增或单调递减的，那么它是单调的。
如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
当给定的数组 A 是单调数组时返回 true，否则返回 false。

示例 1：
输入：[1,2,2,3]
输出：true

示例 2：
输入：[6,5,4,4]
输出：true

示例 3：
输入：[1,3,2]
输出：false

示例 4：
输入：[1,2,4,5]
输出：true

示例 5：
输入：[1,1,1]
输出：true
 
提示：
1 <= A.length <= 50000
-100000 <= A[i] <= 100000
'''

# import lib
from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:

        # 解法一：对列表进行做减法，然后将结果集存放在一个中间数组中，
        # 如果是单调递增数列，那么结果集中的最小值都 >= 0
        # 如果是单调递减数列，那么结果集中的最大值都 <= 0
        # if not A:
        #     return False
        # if len(A) <= 1:
        #     return True
        # result = []
        # for inx in range(1, len(A)):
        #     result.append(A[inx] - A[inx - 1])
        # return min(result) >= 0 or max(result) <= 0

        # 解法二：如果是一个单调数列，对数列进行排序，然后进行copy，然后对排序后的数列进行翻转，
        # 那么当前数列要么和排序后的数列相等，要么和翻转后的数列相等
        B = sorted(A)
        C = B[:]
        C.reverse()
        return (A == B or C == A)

        # 解法三：通过All函数求解
        # return all([A[i + 1] <= A[i] for i in range(len(A) - 1)]) or all([A[i + 1] >= A[i] for i in range(len(A) - 1)])



solution = Solution()
print(solution.isMonotonic([1, 2, 4, 6]))
