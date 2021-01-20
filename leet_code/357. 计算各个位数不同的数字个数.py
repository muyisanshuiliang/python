"""
给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10n 。

示例:
输入: 2
输出: 91
解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。
"""


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        res = 10
        k = 9
        temp = 9
        for _ in range(2, min(n + 1, 11)):
            temp *= k
            k -= 1
            res += temp
        return res


print(Solution().countNumbersWithUniqueDigits(4))
