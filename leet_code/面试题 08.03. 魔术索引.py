class Solution(object):
    def findMagicIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums or len(nums) == 0:
        #     return -1
        # if len(nums) == 1:
        #     return 0
        # for item_inx, item_val in enumerate(nums):
        #     if item_val == item_inx:
        #         return item_inx
        # return -1

        if not nums:
            return -1
        if nums[0] == 0:
            return 0
        p, n = 0, len(nums)
        while p < n:
            if nums[p] > p:
                p = nums[p]
            elif nums[p] == p:
                return p
            else:
                p += 1
        return -1
        # return next(iter(i for i, num in enumerate(nums) if i == num), -1)


nums = [0, 2, 3, 4, 5]
solution = Solution()
print(solution.findMagicIndex(nums))

print(i for i, num in enumerate(nums) if i == num)
