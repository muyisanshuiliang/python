from typing import List


class Solution:
    def massage(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        pre_profit = nums[0]
        pre_pre_profit = 0
        index = 1
        while index < len(nums):
            cur_profit = max(pre_profit, pre_pre_profit + nums[index])
            pre_pre_profit = pre_profit
            pre_profit = cur_profit
            index += 1
        return pre_profit


solution = Solution()
print(solution.massage([1, 2, 3, 1]))
print(solution.massage([2, 7, 9, 3, 1]))
print(solution.massage([2, 1, 4, 5, 3, 1, 1, 3]))
print(solution.massage([1, 1]))
