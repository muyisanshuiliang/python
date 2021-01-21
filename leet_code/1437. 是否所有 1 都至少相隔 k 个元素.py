"""
给你一个由若干 0 和 1 组成的数组 nums 以及整数 k。如果所有 1 都至少相隔 k 个元素，则返回 True ；否则，返回 False 。

示例 1：
输入：nums = [1,0,0,0,1,0,0,1], k = 2
输出：true
解释：每个 1 都至少相隔 2 个元素。

示例 2：
输入：nums = [1,0,0,1,0,1], k = 2
输出：false
解释：第二个 1 和第三个 1 之间只隔了 1 个元素。

示例 3：
输入：nums = [1,1,1,1,1], k = 0
输出：true

示例 4：
输入：nums = [0,1,0,1], k = 1
输出：true
"""
from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # if k == 0:
        #     return True
        # temp_index = -1
        # for item_inx, item_val in enumerate(nums):
        #     if temp_index == -1:
        #         if item_val == 1:
        #             temp_index = 0
        #         continue
        #     if item_val == 0:
        #         temp_index += 1
        #     else:
        #         if temp_index < k:
        #             return False
        #         else:
        #             temp_index = 0
        # return True

        if k == 0:
            return True
        start_index = -1
        for item_inx, item_val in enumerate(nums):
            if item_val == 0:
                continue
            if start_index == -1:
                start_index = item_inx
            else:
                if item_inx - start_index - 1 < k:
                    return False
                else:
                    start_index = item_inx
        return True


print(Solution().kLengthApart(nums=[0,0,1, 0, 0, 1, 0, 1], k=2))
print(Solution().kLengthApart(nums=[1, 0, 0, 0, 1, 0, 0, 1], k=2))
