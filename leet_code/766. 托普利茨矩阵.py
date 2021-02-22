#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   766. 托普利茨矩阵.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/2/22 15:02   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------
给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false 。
如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。

示例 1：
输入：matrix = [[1,2,3,4],
               [5,1,2,3],
               [9,5,1,2]]
输出：true
解释：
在上述矩阵中, 其对角线为:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。
各条对角线上的所有元素均相同, 因此答案是 True 。

示例 2：
输入：matrix = [[1,2],[2,2]]
输出：false
解释：
对角线 "[1, 2]" 上的元素不同。

提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 20
0 <= matrix[i][j] <= 99
'''

# import lib
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # 列表的切片是含头不含尾
        # 从首行开始，对[:-1]依次与下行的[1:]进行比较，只要有一组不相等即不是托普利茨矩阵，然后返回即可
        for i in range(len(matrix) - 1):
            if matrix[i][:-1] != matrix[i + 1][1:]:
                return False
        return True


solution = Solution()
print(solution.isToeplitzMatrix(matrix=[[1, 2, 3, 4],
                                        [5, 1, 2, 3],
                                        [9, 5, 1, 2],
                                        [4, 9, 5, 1],
                                        [7, 4, 9, 5]]))