#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LCP 01. 猜数字.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/12 12:22   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
小A 和 小B 在玩猜数字。小B 每次从 1, 2, 3 中随机选择一个，小A 每次也从 1, 2, 3 中选择一个猜。他们一共进行三次这个游戏，请返回 小A 猜对了几次？
输入的guess数组为 小A 每次的猜测，answer数组为 小B 每次的选择。guess和answer的长度都等于3。

示例 1：
输入：guess = [1,2,3], answer = [1,2,3]
输出：3
解释：小A 每次都猜对了。

示例 2：
输入：guess = [2,2,3], answer = [3,2,1]
输出：1
解释：小A 只猜对了第二次。

限制：
guess 的长度 = 3
answer 的长度 = 3
guess 的元素取值为 {1, 2, 3} 之一。
answer 的元素取值为 {1, 2, 3} 之一。
通过次数70,717提交次数83,902
'''

# import lib
from typing import List


class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        return sum(guess[i] == answer[i] for i in range(len(guess)))


solution = Solution()
print(solution.game(guess=[1, 2, 3], answer=[1, 2, 3]))