#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   59. 螺旋矩阵 II.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/16 9:38   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

示例 1：
输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]

示例 2：
输入：n = 1
输出：[[1]]

提示：
1 <= n <= 20
'''

# import lib
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # if n == 1:
        #     return [[1]]
        # # 分别代表左，右，上，下，边界
        # left, right, up, down = 0, n - 1, 0, n - 1
        # dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # # 分别代表当前值，及其索引值，y是一维的索引，x是二维的索引
        # cur_number, x, y = 1, 0, 0
        # res = [[0] * n for _ in range(n)]
        # total = n * n
        # # 0，1，2，3分別代表向右，下，左，上移动
        # sign = 0
        # while cur_number <= total:
        #     res[y][x] = cur_number
        #     if sign == 0 and x == right:
        #         sign = 1
        #         up += 1
        #     elif sign == 1 and y == down:
        #         sign = 2
        #         right -= 1
        #     elif sign == 2 and x == left:
        #         sign = 3
        #         down -= 1
        #     elif sign == 3 and y == up:
        #         sign = 0
        #         left += 1
        #     x += dirs[sign][1]
        #     y += dirs[sign][0]
        #     cur_number += 1
        # return res
        res = [[0] * n for _ in range(n)]
        left, right, top, down, cur_val = 0, n - 1, 0, n - 1, 1
        while True:
            # 向右移动，横坐标（二维坐标在【左，右】之间）
            for i in range(left, right + 1):
                res[top][i] = cur_val
                cur_val += 1
            # 向右移动完毕，上边界缩小一行
            top += 1
            if top > down:
                break

            # 向下移动，纵坐标（一维坐标在【上，下】之间）
            for i in range(top, down + 1):
                res[i][right] = cur_val
                cur_val += 1
            # 向下移动完毕，右边界缩小一列
            right -= 1
            if left > right:
                break

            # 向左移动，横坐标（二维坐标在【右，左】之间）
            for i in range(right, left - 1, -1):
                res[down][i] = cur_val
                cur_val += 1
            # 向左移动完毕，下边界缩小一行
            down -= 1
            if top > down:
                break

            # 向上移动，纵坐标（一维坐标在【下，上】之间）
            for i in range(down, top - 1, -1):
                res[i][left] = cur_val
                cur_val += 1
            # 向上移动完毕，右边界缩小一列
            left += 1
            if left > right:
                break
        return res


solution = Solution()
print(solution.generateMatrix(3))
