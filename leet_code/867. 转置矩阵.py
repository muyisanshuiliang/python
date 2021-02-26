#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   867. 转置矩阵.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/2/25 11:45   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------
给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。
矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[1,4,7],[2,5,8],[3,6,9]]

示例 2：
输入：matrix = [[1,2,3],[4,5,6]]
输出：[[1,4],[2,5],[3,6]]
 
提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109
'''

# import lib
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = matrix.__len__()
        n = matrix[0].__len__()
        result = [[0] * m for item in range(n)]
        print(result)
        i = 0
        while i < n:
            j = 0
            while j < m:
                result[i][j] = matrix[j][i]
                j += 1
            i += 1
        return result


solution = Solution()
print(solution.transpose(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(solution.transpose(matrix=[[1, 2, 3], [4, 5, 6]]))
