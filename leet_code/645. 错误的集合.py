"""
集合 S 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。
给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
进阶：你可以实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案吗？
"""


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # global error_key, dup
        # nums_dict = dict(Counter(nums))
        # for item in list(range(1, len(nums) + 1)):
        #     num_count = nums_dict.get(item, 0)
        #     if num_count == 0:
        #         dup = item
        #     elif num_count == 2:
        #         error_key = item
        # return [dup, error_key]

        # 求和的方式巧解
        n1 = sum(nums) - sum(set(nums))  # 找出重复的数字
        n2 = sum(range(len(nums) + 1)) - sum(set(nums))  # 找出缺失的数字
        return [n1, n2]



# nums = [3, 2, 3, 4, 6, 5]
solution = Solution()
# print(solution.findErrorNums([1, 2, 2, 4]))
# print(solution.findErrorNums([1, 1]))
# print(solution.findErrorNums([2, 2]))
print(solution.findErrorNums([2, 3, 2]))
