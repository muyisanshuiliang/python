#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1052. 爱生气的书店老板.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/2/23 16:07   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------
今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。
在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一分钟的顾客就会不满意，
不生气则他们是满意的。书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。
请你返回这一天营业下来，最多有多少客户能够感到满意的数量。
 
示例：
输入：customers = [1,0,1,2,1,1,7,5],
        grumpy = [0,1,0,1,0,1,0,1], X = 3
输出：16
解释：
书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
 
提示：
1 <= X <= customers.length == grumpy.length <= 20000
0 <= customers[i] <= 1000
0 <= grumpy[i] <= 1
'''

# import lib
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # 解题思路还是滑动窗口的概念
        """
         retain_cus:记录滑动窗口内挽留的顾客数量
         max_retain_cus:记录整个过程中最大的挽留顾客数量
         result:存储最终的结果
         left:左指针
         right:右指针
        """
        retain_cus, max_retain_cus, result, left, right, start_index = 0, 0, 0, 0, 0, 0
        while right < len(grumpy):
            # 累加本身就满意的顾客
            if grumpy[right] == 0:
                result += customers[right]
            # 如果右指针为不满意的顾客，将其累加到挽留顾客的数量中去
            if grumpy[right] == 1:
                retain_cus += customers[right]

            # 如果左右指针之间的差值大于等于X
            if right - left >= X:
                # 如果左指针遇到的顾客为不满意，那么在滑动窗口右移的时候将其从 retain_cus 中移除
                if grumpy[left] == 1:
                    retain_cus -= customers[left]
                # 如果当前滑动窗口挽留人数大于最大挽留人数，记录起始索引
                if retain_cus > max_retain_cus:
                    start_index = left + 1
                # 移动滑动窗口
                left += 1
            # 修改最大挽留顾客的数量
            max_retain_cus = max(max_retain_cus, retain_cus)
            right += 1
        print(start_index)
        # 本身满意的数量+最大挽留的数量即为返回的结果
        return result + max_retain_cus


solution = Solution()
print(solution.maxSatisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5],
                            grumpy=[0, 1, 0, 1, 0, 1, 0, 1], X=3))
print(solution.maxSatisfied(customers=[3], grumpy=[1], X=1))
print(solution.maxSatisfied([4, 10, 10], [1, 1, 0], 2))
