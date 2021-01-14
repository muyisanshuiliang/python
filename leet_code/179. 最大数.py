import functools
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ''

        class LargerNumKey(str):
            def sort_key(a, b):
                return a + b > b + a

        # nums.sort(key=functools.cmp_to_key(sort_key))
        # if nums[0] == 0:
        #     return '0'
        # # print(nums)
        # nums = [str(item) for item in nums]
        # return ''.join(nums)

        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey,reverse=True))
        return '0' if largest_num[0] == '0' else largest_num


print(Solution().largestNumber(nums=[3, 30, 34, 5, 9]))
