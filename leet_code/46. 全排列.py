"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return list(itertools.permutations(nums))
        res = []

        def backtrack(nums, tmp):
            # 如果集合已经遍历完毕，将当前元素追加到结果集中，递归结束
            if not nums:
                res.append(tmp)
                return
            # 如果结果集还存在，则遍历结果集
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res


nums = [1, 2, 3]
print(Solution().permute(nums))
print(list(itertools.permutations(nums, 2)))
