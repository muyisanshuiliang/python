#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   832. 翻转图像.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/2/24 15:43   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------
给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。
反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。

示例 1：
输入：[[1,1,0],[1,0,1],[0,0,0]]
输出：[[1,0,0],[0,1,0],[1,1,1]]
解释：首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
     然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]

示例 2：
输入：[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
输出：[[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
解释：首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]；
     然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
 
提示：
1 <= A.length = A[0].length <= 20
0 <= A[i][j] <= 1
'''

# import lib
from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:

        # 解法一：笨办法
        # result = []
        # for y in range(len(A)):
        #     x_l = list(range(len(A[y])))
        #     x_l.reverse()
        #     x_result = []
        #     for x in x_l:
        #         if A[y][x] == 1:
        #             x_result.append(0)
        #         else:
        #             x_result.append(1)
        #     result.append(x_result)
        # return result

        # 解法二：先翻转，再取值
        # rows = len(A)
        # cols = len(A[0])
        # for row in range(rows):
        #     A[row] = A[row][::-1]
        #     for col in range(cols):
        #         A[row][col] ^= 1
        # return A

        # 解法三：翻转的同时修改数值，A, B = 1 - B, 1 - A
        # N = len(A)
        # for i in range(N):
        #     for j in range((N + 1) // 2):
        #         A[i][j], A[i][N - 1 - j] = 1 - A[i][N - 1 - j], 1 - A[i][j]
        # return A

        # 解法四：额外的存储空间
        # M, N = len(A), len(A[0])
        # res = [[0] * N for _ in range(M)]
        # for i in range(M):
        #     for j in range(N):
        #         res[i][j] = 1 - A[i][N - 1 - j]
        # return res

        return [[1 - A[i][len(A) - 1 - j] for j in range(len(A[i]))] for i in range(len(A))]


l = list(range(5))
l.reverse()
print(l)

solution = Solution()
print(solution.flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
print(solution.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
