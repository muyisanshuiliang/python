class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # index = 0
        # while index < len(nums) - 1:
        #     # 任何数与本身异或为0
        #     if nums[index] ^ nums[index + 1] != 0:
        #         return nums[index]
        #     index += 2
        # # 如果停止循环的位置刚好为倒数第一个数，说明最后一个数为非重复数
        # if index == len(nums) - 1:
        #     return nums[-1]
        # # 否则数据无重复数
        # return None

        # 左侧索引 0
        l = 0
        # 右侧索引 8
        h = len(nums) - 1
        while l < h:
            # 中间索引 4
            mid = int((l + h) / 2)
            # 索引是从0 开始的，如果中间索引能够被2整除，说明非重复元素在前半段，故
            if mid % 2 != 0:
                mid -= 1
            if nums[mid] != nums[mid + 1]:
                h = mid
            else:
                l = mid + 2
        return nums[l]


nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
solution = Solution()
print(solution.singleNonDuplicate(nums))
