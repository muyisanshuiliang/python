"""
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:
输入: [1,2,3]
输出: 6

示例 2:
输入: [1,2,3,4]
输出: 24

注意:
给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
"""
import sys
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 3:
            return nums[0] * nums[1] * nums[2]
        # 排序算法
        # nums.sort()
        # return max(nums[0] * nums[1] * nums[length - 1], nums[length - 3] * nums[length - 2] * nums[length - 1])

        # max1 = max(nums)
        # min1 = min(nums)
        # nums.remove(max1)
        # max2 = max(nums)
        # nums.remove(max2)
        # max3 = max(nums)
        # nums.remove(min1)
        # min2 = min(nums)
        # return max(max1 * max2 * max3, max1 * min1 * min2)
        # 线性扫描，求的最大三个值和最小的两个值
        max1 = max2 = max3 = -sys.maxsize - 1
        min1 = min2 = sys.maxsize

        for item in range(length):
            if nums[item] < min1:
                min2, min1 = min1, nums[item]
            elif nums[item] < min2:
                min2 = nums[item]

            if nums[item] > max1:
                max3, max2, max1 = max2, max1, nums[item]
            elif nums[item] > max2:
                max3, max2 = max2, nums[item]
            elif nums[item] > max3:
                max3 = nums[item]
        return max(max1 * max2 * max3, max1 * min1 * min2)


print(Solution().maximumProduct([2001, 1, -1000, -2000, 2, 3, 4]))

nums = [2001, 1, -1000, -2000, 2, 3, 4]
