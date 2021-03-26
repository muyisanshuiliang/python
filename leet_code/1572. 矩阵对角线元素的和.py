#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1572. 矩阵对角线元素的和.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/24 16:47   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。
请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。

示例  1：
输入：mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]
输出：25
解释：对角线的和为：1 + 5 + 9 + 3 + 7 = 25
请注意，元素 mat[1][1] = 5 只会被计算一次。

示例  2：
输入：mat = [[1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1]]
输出：8

示例 3：
输入：mat = [[5]]
输出：5

提示：
n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100
'''

# import lib
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # calculated = []
        # N, M = len(mat), len(mat[0])
        # res = 0
        # i, j = 0, 0
        # while i < N and j < M:
        #     res += mat[i][j]
        #     calculated.append([i, j])
        #     i += 1
        #     j += 1
        #
        # i, j = 0, M - 1
        # while i < N and j >= 0:
        #     if calculated.__contains__([i, j]):
        #         pass
        #     else:
        #         res += mat[i][j]
        #         calculated.append([i, j])
        #     i += 1
        #     j -= 1
        # print(calculated)
        # return res

        # 5*5的矩阵，
        # n = len(mat)
        # total = 0
        # mid = n // 2
        # for i in range(n):
        #     # mat[0][0] + mat[0][5-1-0]
        #     # mat[1][1] + mat[1][5-1-1]
        #     # mat[2][2] + mat[2][5-1-2]
        #     # mat[3][3] + mat[3][5-1-3]
        #     # mat[3][3] + mat[4][5-1-4]
        #     total += mat[i][i] + mat[i][n - 1 - i]
        # # n & 1 如果n是奇数为1，n是偶数为0
        # return total - mat[mid][mid] * (n & 1)

        a = 0
        for i in range(len(mat)):
            a += mat[i][i]
            a += mat[i][len(mat) - 1 - i]
        # 如果是奇数，减去交叉点的数据
        if len(mat) % 2 == 1:
            a -= mat[len(mat) // 2][len(mat) // 2]
        return a


solution = Solution()
print(solution.diagonalSum(mat=[[5]]))
