#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1518. 换酒问题.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/5 16:03   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
小区便利店正在促销，用 numExchange 个空酒瓶可以兑换一瓶新酒。你购入了 numBottles 瓶酒。
如果喝掉了酒瓶中的酒，那么酒瓶就会变成空的。
请你计算 最多 能喝到多少瓶酒。

示例 1：
输入：numBottles = 9, numExchange = 3
输出：13
解释：你可以用 3 个空酒瓶兑换 1 瓶酒。
所以最多能喝到 9 + 3 + 1 = 13 瓶酒。

示例 2：
输入：numBottles = 15, numExchange = 4
输出：19
解释：你可以用 4 个空酒瓶兑换 1 瓶酒。
所以最多能喝到 15 + 3 + 1 = 19 瓶酒。

示例 3：
输入：numBottles = 5, numExchange = 5
输出：6

示例 4：
输入：numBottles = 2, numExchange = 3
输出：2
 
提示：
1 <= numBottles <= 100
2 <= numExchange <= 100
'''


# import lib
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        def count(x):
            # 如果用于换酒瓶子的数量小于换所需求的数量，返回0
            if x < numExchange:
                return 0
            # 能够换的数量
            exchange = x // numExchange
            # 剩余未换的数量
            empty_bottle = x % numExchange
            # 本次换的+递归后续换的，就为总共换的数量
            return exchange + count(empty_bottle + exchange)

        return count(numBottles) + numBottles


solution = Solution()
# print(solution.numWaterBottles(numBottles=2, numExchange=3))
print(solution.numWaterBottles(numBottles=5, numExchange=5))
print(solution.numWaterBottles(numBottles=15, numExchange=4))
print(solution.numWaterBottles(numBottles=9, numExchange=3))
