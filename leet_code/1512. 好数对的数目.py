"""
给你一个整数数组 nums 。
如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。
返回好数对的数目。

示例 1：
输入：nums = [1,2,3,1,1,3]
输出：4
解释：有 4 组好数对，分别是 (0,3), (0,4), (3,4), (2,5) ，下标从 0 开始

示例 2：
输入：nums = [1,1,1,1]
输出：6
解释：数组中的每组数字都是好数对

示例 3：
输入：nums = [1,2,3]
输出：0
"""
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums_dict = dict(zip(nums, [0] * len(nums)))
        print(nums_dict)
        item_index = 0
        while item_index < len(nums):
            nums_dict[nums[item_index]] = nums_dict[nums[item_index]] + 1
            item_index += 1
        print(nums_dict)

        def num(n):
            if n == 0:
                return 0
            else:
                return n + num(n - 1)

        return sum(num(item - 1) for item in nums_dict.values())

        # count = 0
        # for i, v in enumerate(nums):
        #     left_nums = nums[i + 1:]
        #     for l in left_nums:
        #         if v == l:
        #             count += 1
        # return count


print(Solution().numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3]))
