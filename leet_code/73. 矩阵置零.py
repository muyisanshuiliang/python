#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   73. 矩阵置零.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/22 10:04   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

进阶：
一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个仅使用常量空间的解决方案吗？

示例 1：
输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]

示例 2：
输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

提示：
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
'''

# import lib
import copy
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # high = len(matrix)
        # width = len(matrix[0])
        # high_set = set()
        # width_set = set()
        # for high_item in range(0, high):
        #     for width_item in range(0, width):
        #         if matrix[high_item][width_item] != 0:
        #             continue
        #         high_set.add(high_item)
        #         width_set.add(width_item)
        # print(high_set)
        # print(width_set)
        # if high_set:
        #     for high_item in high_set:
        #         matrix[high_item] = [0] * width
        # print(matrix)
        # if width_set:
        #     for width_item in width_set:
        #         for high_item in range(0, high):
        #             matrix[high_item][width_item] = 0
        # print(matrix)

        # # 解法一：复制数组，进行判断赋值
        # if not matrix or not matrix[0]:
        #     return
        # M, N = len(matrix), len(matrix[0])
        # matrix_copy = copy.deepcopy(matrix)
        # for i in range(M):
        #     for j in range(N):
        #         if matrix_copy[i][j] == 0:
        #             for k in range(M):
        #                 matrix[k][j] = 0
        #             for k in range(N):
        #                 matrix[i][k] = 0
        # print(matrix)

        # 解法二：
        if not matrix or not matrix[0]:
            return
        M, N = len(matrix), len(matrix[0])
        row0, col0 = False, False
        # 获取第0行中是否存在0
        for i in range(M):
            if matrix[i][0] == 0:
                col0 = True
                break
        # 获取第0列中是否存在0
        for j in range(N):
            if matrix[0][j] == 0:
                row0 = True
                break
        # 将非0列0行的0转移到第0行0列
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # 如果当前元素对应的行首或者列首为0，那么当前位置都应该是0
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # 如果第0行0列存在0元素，修改对应的行列值
        if row0:
            for j in range(N):
                matrix[0][j] = 0
        if col0:
            for i in range(M):
                matrix[i][0] = 0
        print(matrix)


solution = Solution()
print(solution.setZeroes([[1, 1, 2, 1], [3, 0, 5, 2], [1, 3, 1, 5]]))
