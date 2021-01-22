"""
给定一个 row x col 的二维网格地图 grid ，其中：grid[i][j] = 1 表示陆地， grid[i][j] = 0 表示水域。
网格中的格子 水平和垂直 方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

示例 1：
输入：grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
输出：16
解释：它的周长是上面图片中的 16 个黄色的边

示例 2：
输入：grid = [[1]]
输出：4

示例 3：
输入：grid = [[1,0]]
输出：4
 
提示：
row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] 为 0 或 1
"""
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        high = len(grid)
        width = len(grid[0])
        grid_count = 0
        repeat_edge = 0
        for item_high in range(0, high):
            for item_width in range(0, width):
                if grid[item_high][item_width] == 1:
                    grid_count += 1
                    if item_high != 0:
                        if grid[item_high - 1][item_width] == 1:
                            repeat_edge += 1
                    if item_width != 0:
                        if grid[item_high][item_width - 1] == 1:
                            repeat_edge += 1
        # 每一个岛屿是四个边，如果一旦两个岛屿相邻，那么就会减少两个边的长度
        return grid_count * 4 - repeat_edge * 2


# print(Solution().islandPerimeter(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
print(Solution().islandPerimeter(grid=[[ 1, 0]]))
