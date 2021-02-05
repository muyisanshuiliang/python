"""
对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。
给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。

示例 1：
输入：A = [1,2,0,0], K = 34
输出：[1,2,3,4]
解释：1200 + 34 = 1234

示例 2：
输入：A = [2,7,4], K = 181
输出：[4,5,5]
解释：274 + 181 = 455

示例 3：
输入：A = [2,1,5], K = 806
输出：[1,0,2,1]
解释：215 + 806 = 1021

示例 4：
输入：A = [9,9,9,9,9,9,9,9,9,9], K = 1
输出：[1,0,0,0,0,0,0,0,0,0,0]
解释：9999999999 + 1 = 10000000000
 

提示：
1 <= A.length <= 10000
0 <= A[i] <= 9
0 <= K <= 10000
如果 A.length > 1，那么 A[0] != 0
"""
from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        # 将整数变成列表
        K = list(map(int, str(K)))
        # 用于存放结果集
        res = []
        # 两个列表的最大索引值
        i, j = len(A) - 1, len(K) - 1
        # 进位值
        carry = 0

        # 从列表的右端往左端遍历元素，多元素进行加法计算
        while i >= 0 and j >= 0:
            res.append(A[i] + K[j] + carry)
            # 获取余数和值
            res[-1], carry = res[-1] % 10, res[-1] // 10
            i -= 1
            j -= 1
        # 对未循环完的元素进行处理
        while i >= 0:
            res.append(A[i] + carry)
            res[-1], carry = res[-1] % 10, res[-1] // 10
            i -= 1
        while j >= 0:
            res.append(K[j] + carry)
            res[-1], carry = res[-1] % 10, res[-1] // 10
            j -= 1
        # 如果进位不为0，
        if carry:
            res.append(1)
        # 反转列表，从高位到低位
        return res[::-1]


        # i = len(A) - 1
        # while K:
        #     A[i] += K
        #     K, A[i] = A[i] // 10, A[i] % 10
        #     i -= 1
        #
        #     if i < 0 and K:
        #         A.insert(0, 0)
        #         i = 0
        # return A

        # return map(int, str(int(''.join(map(str, A))) + K))


# print(Solution().addToArrayForm(A=[9, 9, 9, 9, 9, 9, 9, 9, 9, 9], K=1))
print(Solution().addToArrayForm(A=[1, 2, 7, 9], K=9834))
