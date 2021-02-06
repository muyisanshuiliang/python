#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1423. 可获得的最大点数.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/2/6 14:34   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------
几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。
每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。
你的点数就是你拿到手中的所有卡牌的点数之和。
给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。

示例 1：
输入：cardPoints = [1,2,3,4,5,6,1], k = 3
输出：12
解释：第一次行动，不管拿哪张牌，你的点数总是 1 。但是，先拿最右边的卡牌将会最大化你的可获得点数。最优策略是拿右边的三张牌，最终点数为 1 + 6 + 5 = 12 。

示例 2：
输入：cardPoints = [2,2,2], k = 2
输出：4
解释：无论你拿起哪两张卡牌，可获得的点数总是 4 。

示例 3：
输入：cardPoints = [9,7,7,9,7,7,9], k = 7
输出：55
解释：你必须拿起所有卡牌，可以获得的点数为所有卡牌的点数之和。

示例 4：
输入：cardPoints = [1,1000,1], k = 1
输出：1
解释：你无法拿到中间那张卡牌，所以可以获得的最大点数为 1 。

示例 5：
输入：cardPoints = [1,79,80,1,1,1,200,1], k = 3
输出：202
 
提示：
1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length
'''

# import lib
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints)
        if not cardPoints or size == 0 or k == 0:
            return 0
        if size <= k:
            return sum(cardPoints)
        pre_res = temp_pre_res = sum(cardPoints[:k])
        # ord_res = temp_ord_res = sum(cardPoints[-k:])
        for item in range(k):
            temp_pre_res = temp_pre_res - cardPoints[k - item - 1] + cardPoints[-(item + 1)]
            if temp_pre_res > pre_res:
                pre_res = temp_pre_res
            # temp_ord_res = temp_ord_res - cardPoints[-(k - item)] + cardPoints[item]
            # if temp_ord_res > ord_res:
            #     ord_res = temp_ord_res
        # return pre_res if pre_res >= ord_res else ord_res
        return pre_res


# print(Solution().maxScore(cardPoints=[1, 2, 3, 4, 5, 6, 1, 3, 4], k=4))
print(Solution().maxScore([96, 90, 41, 82, 39, 74, 64, 50, 30], 8))
