#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   354. 俄罗斯套娃信封问题.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/5 11:15   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------
给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。
当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
注意：不允许旋转信封。

示例 1：
输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出：3
解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

示例 2：
输入：envelopes = [[1,1],[1,1],[1,1]]
输出：1
 
提示：
1 <= envelopes.length <= 5000
envelopes[i].length == 2
1 <= wi, hi <= 104
'''

# import lib
import bisect
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # 解法一：逐一对元素进行比较
        # if not envelopes:
        #     return 0
        # N = len(envelopes)
        # envelopes.sort()
        # dp = [1] * N
        # for i in range(N):
        #     for j in range(i):
        #         # 对前面的每一个元素进行对比，如果符合套娃条件就在原来的套娃的数量上+1
        #         if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # # 返回最大的套娃数量
        # return max(dp)

        # 解法二：取巧比较
        # if not envelopes:
        #     return 0
        # N = len(envelopes)
        # # 第一个纬度递增，第二个纬度递减，这样判断第二个纬度的最大递增数列长度即为套娃的最大数量
        # envelopes.sort(key=lambda x: (x[0], -x[1]))
        # print(envelopes)
        # dp = [1] * N
        # for i in range(N):
        #     for j in range(i):
        #         if envelopes[j][1] < envelopes[i][1]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)

        # 解法三：
        if not envelopes:
            return 0
        n = len(envelopes)
        # 第一纬度升序，第二维度降序
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        print(envelopes)
        f = [envelopes[0][1]]
        # 依次放入第二维度中较小的数，
        for i in range(1, n):
            # 海象运算符，如果第二纬度的元素大于前一个的，直接追加元素即可
            if (num := envelopes[i][1]) > f[-1]:
                f.append(num)
            else:
                # 二分查找，在f中找到num的插入点，左侧元素全部是<num，右侧的元素全部是>num,
                index = bisect.bisect_left(f, num)
                f[index] = num
        return len(f)


solution = Solution()
# print(solution.maxEnvelopes(envelopes=[[30, 50], [12, 2], [3, 4], [12, 15]]))
print(solution.maxEnvelopes(envelopes=[[2, 3], [5, 4], [6, 7], [6, 6], [8, 7], [8, 8], [9, 7], [7, 7], [9, 8]]))
