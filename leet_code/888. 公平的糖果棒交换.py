#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   888. 公平的糖果棒交换.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/2/1 9:30   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------
爱丽丝和鲍勃有不同大小的糖果棒：A[i] 是爱丽丝拥有的第 i 根糖果棒的大小，B[j] 是鲍勃拥有的第 j 根糖果棒的大小。
因为他们是朋友，所以他们想交换一根糖果棒，这样交换后，他们都有相同的糖果总量。（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）
返回一个整数数组 ans，其中 ans[0] 是爱丽丝必须交换的糖果棒的大小，ans[1] 是 Bob 必须交换的糖果棒的大小。
如果有多个答案，你可以返回其中任何一个。保证答案存在。

示例 1：
输入：A = [1,1], B = [2,2]
输出：[1,2]

示例 2：
输入：A = [1,2], B = [2,3]
输出：[1,2]

示例 3：
输入：A = [2], B = [1,3]
输出：[2,3]

示例 4：
输入：A = [1,2,5], B = [2,4]
输出：[5,4]
 
提示：
1 <= A.length <= 10000
1 <= B.length <= 10000
1 <= A[i] <= 100000
1 <= B[i] <= 100000
保证爱丽丝与鲍勃的糖果总量不同。
答案肯定存在。
'''

# import lib
from collections import defaultdict
from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        # a_sum = sum(A)
        # b_sum = sum(B)
        # if a_sum == b_sum:
        #     return [0, 0]
        # a_dict = dict(zip(range(len(A)), A))
        # print(a_dict)
        # for item in A:
        #     b_val = (b_sum - a_sum + 2 * item) // 2
        #     if B.__contains__(b_val):
        #         return [item, b_val]
        # return []

        diff = (sum(B) - sum(A)) // 2
        dict_b = {i: True for i in B}
        dict_b = defaultdict(bool, dict_b)
        # （a_sum - xa + xb） = (b_sum - xb + xa) ====> xa = diff + xb
        for item_val in A:
            if dict_b[item_val + diff]:
                return [item_val, item_val + diff]
        return []


print(Solution().fairCandySwap(A=[1, 2, 5], B=[2, 4]))
print(Solution().fairCandySwap(A = [1,1], B = [2,2]))
