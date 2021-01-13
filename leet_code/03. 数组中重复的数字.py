class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums:
        #     return None
        # n = len(nums)
        # if n == 1:
        #     return None
        # dict_number = {}
        # for item in nums:
        #     if dict_number.get(item, 0) == 1:
        #         return item
        #     else:
        #         dict_number[item] = 1
        # return None
        L = (max(nums) + 1) * [0]
        for n in nums:
            if L[n] == 1:
                return n
            else:
                L[n] += 1
        return None
        # for num, i in enumerate(L):
        #     if i > 1:
        #         return num


solution = Solution()
nums = [2, 3, 1, 0, 2, 5, 3, 12]
print(solution.findRepeatNumber(nums))
