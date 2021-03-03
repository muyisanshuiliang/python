#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   304. 二维区域和检索 - 矩阵不可变.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/3 16:14   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------
给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。

示例：
给定 matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

提示：
你可以假设矩阵不可变。
会多次调用 sumRegion 方法。
你可以假设 row1 ≤ row2 且 col1 ≤ col2 。
'''

# import lib
from typing import List


class NumMatrix:

    # def __init__(self, matrix: List[List[int]]):
    #     self.__matrix = matrix
    #     self.__row = len(self.__matrix) if self.__matrix else 0
    #     self.__col = len(self.__matrix[0]) if self.__matrix else 0
    #
    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     result = 0
    #     row1 = row1 if row1 >= 0 else 0
    #     row2 = row2 if row2 >= 0 else 0
    #     row1 = row1 if row1 < self.__row else self.__row
    #     row2 = row2 if row2 < self.__row else self.__row
    #     col1 = col1 if col1 >= 0 else 0
    #     col2 = col2 if col2 >= 0 else 0
    #     col1 = col1 if col1 < self.__col else self.__col
    #     col2 = col2 if col2 < self.__col else self.__col
    #     while row1 <= row2:
    #         temp = self.__matrix[row1]
    #         result += sum(temp[col1: col2 + 1])
    #         row1 += 1
    #     return result
    def __init__(self, matrix: List[List[int]]):
        # 求取矩阵的横纵坐标最大值
        if not matrix or not matrix[0]:
            M, N = 0, 0
        else:
            M, N = len(matrix), len(matrix[0])
        # 初始预处理数组
        self.preSum = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M):
            for j in range(N):
                self.preSum[i + 1][j + 1] = self.preSum[i][j + 1] + self.preSum[i + 1][j] - self.preSum[i][j] + \
                                            matrix[i][j]
        # print(self.preSum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preSum[row2 + 1][col2 + 1] - self.preSum[row2 + 1][col1] - self.preSum[row1][col2 + 1] + \
               self.preSum[row1][col1]


matrix = NumMatrix(matrix=[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(matrix.sumRegion(2, 1, 4, 3))
print(matrix.sumRegion(1, 1, 2, 2))
print(matrix.sumRegion(1, 2, 2, 4))
