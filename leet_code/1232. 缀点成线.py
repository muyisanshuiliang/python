"""
在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。
请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。

输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
输出：true

输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
输出：false

思路：保持斜率相等是解题的关键
"""

from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # if not coordinates:
        #     return False
        # length = len(coordinates)
        # if length == 1:
        #     return True
        # pre_x = coordinates[0][0]
        # pre_y = coordinates[0][1]
        # for index in range(1, length - 1):
        #     cur_x = coordinates[index][0]
        #     cur_y = coordinates[index][1]
        #     later_x = coordinates[index + 1][0]
        #     later_y = coordinates[index + 1][1]
        #     if (cur_x - pre_x) * (later_y - cur_y) != (cur_y - pre_y) * (later_x - cur_x):
        #         return False
        #     pre_x = cur_x
        #     pre_y = cur_y
        # return True

        if coordinates is None or len(coordinates) <= 2:
            return True

        dy = coordinates[1][1] - coordinates[0][1]
        dx = coordinates[1][0] - coordinates[0][0]

        for i in range(2, len(coordinates)):
            dy1 = coordinates[i][1] - coordinates[0][1]
            dx1 = coordinates[i][0] - coordinates[0][0]
            if dy * dx1 != dy1 * dx:
                return False

        return True


print(Solution().checkStraightLine(coordinates=[[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
print(Solution().checkStraightLine(coordinates=[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
