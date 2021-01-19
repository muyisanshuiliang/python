"""
面试题 16.17. 连续数列 <====>(剑指 Offer 42、53)
给定一个整数数组，找出总和最大的连续数列，并返回总和。

示例：
输入： [-2,1,-3,4,-1,2,1,-5,4]
输出： 6
解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶：
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = []
        result.append(nums[0])
        for item_inx in range(1, len(nums)):
            # 每一个数据都有两个选择，与前面相连或者自己另立门户！
            # 所以状态转移方程就是这个 dp[i] = Math.max(dp[i - 1] + nums[i],nums[i]);
            result.append(max(nums[item_inx], nums[item_inx] + result[-1]))
        # print(result)
        return max(result)


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
