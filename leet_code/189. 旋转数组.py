class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 1、python技巧
        # if nums is None or len(nums) == 0 or k == 0:
        #     return nums
        # index = 0
        # while index < k:
        #     tail = nums.pop()
        #     nums.insert(0, tail)
        #     index += 1
        # return nums

        # 2、借用临时数组
        # if nums is None or len(nums) == 0 or k == 0:
        #     return nums
        # n = len(nums)
        # # 获取实际移动位置
        # k = k % n
        # generator = (x for x in nums)
        # temp_array = list(generator)
        # for index in list(range(n)):
        #     nums[(index + k) % n] = temp_array[index]
        # return nums

        # 3、数组翻转
        if nums is None or len(nums) == 0 or k == 0:
            return nums
        nums.reverse()
        n = len(nums)
        start_index = k % n
        trance_count = int((n - start_index) / 2)
        x = 0
        while x < trance_count:
            temp = nums[n - x - 1]
            nums[n - x - 1] = nums[start_index + x]
            nums[start_index + x] = temp
            x += 1
        x = 0
        while x < int(start_index / 2):
            temp = nums[start_index - x - 1]
            nums[start_index - x - 1] = nums[x]
            nums[x] = temp
            x += 1
        return nums


nums = [1, 2, 3, 4, 5, 6, 7]
k = 1
solution = Solution()
print(solution.rotate(nums, k))
