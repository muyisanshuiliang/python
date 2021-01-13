class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        indexes = list(range(len(nums) - 1))
        for item_inx in indexes:
            if nums[item_inx] ^ nums[item_inx + 1] == 0:
                if item_inx != 0 or nums[item_inx] == 1:
                    return [nums[item_inx], nums[item_inx] + 1]
                else:
                    return [nums[item_inx] - 1, nums[item_inx]]


# nums = [3, 2, 3, 4, 6, 5]
solution = Solution()
print(solution.findErrorNums([1, 2, 2, 4]))
print(solution.findErrorNums([1, 1]))
print(solution.findErrorNums([2, 2]))
