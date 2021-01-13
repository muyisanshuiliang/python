class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        length = len(nums)
        if length == 1:
            return False
        nums_dict = {}
        for item in nums:
            if nums_dict.get(item, 0) == 1:
                return True
            else:
                nums_dict[item] = 1
        return False


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
solution = Solution()
print(solution.containsDuplicate(nums))
