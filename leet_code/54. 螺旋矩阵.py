#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   54. 螺旋矩阵.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/15 9:37   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''

# import lib
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []
        M, N = len(matrix), len(matrix[0])
        left, right, up, down = 0, N - 1, 0, M - 1
        res = []
        x, y = 0, 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_d = 0
        while len(res) != M * N:
            res.append(matrix[x][y])
            # 表示指针已经移动到最右端，横坐标已经达到最右端
            if cur_d == 0 and y == right:
                # 下一步向下移动，横坐标不变，纵坐标+1变动
                cur_d += 1
                # 上边界缩小一格
                up += 1
            # 表示指针已经移动到最下端，纵坐标已经达到最下端
            elif cur_d == 1 and x == down:
                # 下一步向左移动，纵坐标不变，横坐标-1变动
                cur_d += 1
                # 右边界缩小一格
                right -= 1
            # 表示指针已经移动到最左端，横坐标已经达到最左端
            elif cur_d == 2 and y == left:
                # 下一步向上移动，横坐标不变，纵坐标-1变动
                cur_d += 1
                # 下边界缩小一格
                down -= 1
            # 表示指针已经移动到最上端，纵坐标已经达到最顶端
            elif cur_d == 3 and x == up:
                # 下一步向右移动，纵坐标不变，横坐标+1变动
                cur_d += 1
                # 左边界缩小一格
                left += 1
            cur_d %= 4
            # 实时变动当前坐标的位置
            x += dirs[cur_d][0]
            y += dirs[cur_d][1]
        return res


solution = Solution()
print(solution.spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
