#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1004. 最大连续1的个数 III.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/2/21 14:36   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------
给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。
返回仅包含 1 的最长（连续）子数组的长度。

示例 1：
输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：
[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。

示例 2：
输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。
 
提示：
1 <= A.length <= 20000
0 <= K <= A.length
A[i] 为 0 或 1 
'''

# import lib
from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        if len(A) <= K:
            return len(A)
        max_number = 0
        # 滑动窗口，左右指针以及统计出现的0数量
        left, right, zero_number = 0, 0, 0
        while right < len(A):
            # 如果右指针碰到0，则0的统计数量加1
            if A[right] == 0:
                zero_number += 1
            # 当0出现的次数多余指定数据时，移动左指针，对1进行减少
            if zero_number > K:
                while zero_number > K:
                    left += 1
                    if A[left - 1] == 0:
                        zero_number -= 1
            # 获取连续出现1的最大数据
            max_number = max(max_number, right - left + 1)
            right += 1
        return max_number


solution = Solution()
print(solution.longestOnes(A=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], K=0))
