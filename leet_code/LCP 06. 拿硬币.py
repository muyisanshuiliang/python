#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LCP 06. 拿硬币.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/24 16:58   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
桌上有 n 堆力扣币，每堆的数量保存在数组 coins 中。我们每次可以选择任意一堆,
拿走其中的一枚或者两枚，求拿完所有力扣币的最少次数。

示例 1：
输入：[4,2,1]
输出：4
解释：第一堆力扣币最少需要拿 2 次，第二堆最少需要拿 1 次，第三堆最少需要拿 1 次，总共 4 次即可拿完。

示例 2：
输入：[2,3,10]
输出：8

限制：
1 <= n <= 4
1 <= coins[i] <= 10
'''

# import lib
from typing import List


class Solution:
    def minCount(self, coins: List[int]) -> int:
        # res = 0
        # for item in coins:
        #     res += (item // 2)
        #     if item % 2 != 0:
        #         res += 1
        # return res

        # T = 0
        # for i in coins:
        #     if i % 2 == 1:
        #         T = T + int(i / 2) + 1
        #     else:
        #         T = T + int(i / 2)
        # return T

        return sum((c + 1) // 2 for c in coins)


solution = Solution()
print(solution.minCount([4, 2, 1]))
print(solution.minCount([2, 3, 10]))
