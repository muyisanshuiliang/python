from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0 or len(nums) == 1:
            return None
        # 记录最后一个0和1的索引
        last_zero_index = last_one_index = pre_index = 0
        for item_inx, item_val in enumerate(nums):
            if item_val == 0:
                if pre_index == last_zero_index:
                    pass
                else:
                    last_zero_index += 1
                    nums[last_zero_index] = 0
                    last_one_index += 1
                    nums[last_one_index] = 1
                    nums[item_inx] = 2
            elif item_val == 1:
                if pre_index == last_one_index:
                    pass
                else:
                    last_one_index += 1
                    nums[last_one_index] = 1
                    nums[item_inx] = 2
            pre_index = item_inx
        print(nums)


print(Solution().sortColors([2, 0, 2, 1, 1, 0]))
