class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # result = {}
        # for item_inx, item_val in enumerate(nums):
        #     if item_val > target:
        #         continue
        #     get = result.get(target - item_val, None)
        #     if get is None:
        #         result[item_val] = item_inx
        #     else:
        #         return [item_val, target - item_val]
        # return None

        # for item in nums:
        #     if item > target:
        #         continue
        #     if nums.__contains__(target - item):
        #         return [item, target - item]
        # return None

        left_inx, right_inx = 0, len(nums) - 1
        while left_inx < right_inx:
            # 如果左侧的数大于目标数，则继续向左查找元素
            if nums[right_inx] > target:
                right_inx -= 1
                # 如果左侧的值小于 目标值与右侧值的差值，则左指针朝右移动
            elif nums[left_inx] < target - nums[right_inx]:
                left_inx += 1
            elif nums[left_inx] > target - nums[right_inx]:
                right_inx -= 1
            else:
                return [nums[left_inx], nums[right_inx]]


nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(nums, 9))
