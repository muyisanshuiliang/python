class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums or len(nums) == 0:
        #     return 0
        # l = len(nums)
        # if l == 1:
        #     return nums[0]
        # nums[1] = max(nums[0], nums[1])
        # index = 2
        # while index < l:
        #     nums[index] = max(nums[index - 1], nums[index - 2] + nums[index])
        #     index += 1
        # return nums[-1]

        if not nums:
            return 0

        pre1, pre2 = 0, nums[0]
        cur = pre2
        for i in range(1, len(nums)):
            cur = max(pre2, pre1 + nums[i])
            pre1, pre2 = pre2, cur
        return cur


nums = [2, 1, 1, 2]
solution = Solution()
print(solution.rob(nums))
