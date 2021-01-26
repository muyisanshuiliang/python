"""
给你一个由一些多米诺骨牌组成的列表 dominoes。
如果其中某一张多米诺骨牌可以通过旋转 0 度或 180 度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。
形式上，dominoes[i] = [a, b] 和 dominoes[j] = [c, d] 等价的前提是 a==c 且 b==d，或是 a==d 且 b==c。
在 0 <= i < j < dominoes.length 的前提下，找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i, j) 的数量。

示例：
输入：dominoes = [[1,2],[2,1],[3,4],[5,6]]
输出：1
 
提示：
1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9
"""
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num = [0] * 100
        ret = 0
        for x, y in dominoes:
            # 注意元素的值位于[0,9]之间，我们以两数之和作为元素下标，数据出现的次数作为值
            val = (x * 10 + y if x <= y else y * 10 + x)
            # 等价多米诺骨牌出现的次数 = 当前值 + 以前出现的次数
            ret += num[val]
            # 当前值已出现的次数 + 1
            num[val] += 1
        return ret


print(Solution().numEquivDominoPairs(dominoes=[[1, 2], [2, 1], [3, 4], [5, 6]]))