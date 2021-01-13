class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # count = nums.count(0)
        # if count == 0:
        #     return nums
        # length = len(nums)
        # if length == count:
        #     return nums
        # for _ in list(range(count)):
        #     nums.remove(0)
        # nums.extend([0] * count)
        # return nums

        i = 0
        n = len(nums)
        for x in range(n):
            if not nums[x] == 0:
                nums[i] = nums[x]
                i += 1
        for x in range(i, n):
            nums[x] = 0
        return nums


nums = [0, 1, 0, 3, 12]
# print(nums.count(0))
# nums.remove(0)
# print(nums)
# nums.remove(0)
# print(nums)
solution = Solution()
print(solution.moveZeroes(nums))
