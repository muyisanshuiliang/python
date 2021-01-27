"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

示例 2：
输入：nums = []
输出：[]

示例 3：
输入：nums = [0]
输出：[]

"""
from functools import reduce
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # if not nums or len(nums) < 3:
        #     return []
        # nums.sort()
        # result = []
        # # 最大值小于0或者或者最小值大于0，肯定不存在结果，为什么不取等号，因为避免出现元素均为0的情况
        # if nums[0] > 0 or nums[len(nums) - 1] < 0:
        #     return result
        # # 对结果集进行遍历
        # for item in range(len(nums) - 1):
        #     # 如果当前值指针值大于0且与上一个值相等，如果找到结果集也是重复集，故跳过本次循环
        #     if item > 0 and nums[item] == nums[item - 1]:
        #         continue
        #     # 左右指针，左指针为当前指针+1，右指针为数组长度-1
        #     left_index, right_index = item + 1, len(nums) - 1
        #     # 只有左指针小于右指针才会出现结果集
        #     while left_index < right_index:
        #         # 如果三数之和为0，那当前数据就是结果集
        #         if nums[item] + nums[left_index] + nums[right_index] == 0:
        #             # 追加结果接
        #             result.append([nums[item], nums[left_index], nums[right_index]])
        #             # 避免重复，如果右指针的值与前一个值相等，右指针持续左移，持续找到不相等的值为止
        #             """
        #             eg：[-1,0,0,1,1,1,1,2]
        #             当找到第一个==0的结果是[-1,0,1(这个1的索引是6)]
        #             如果继续循环会一次找到结果重复的结果集：
        #             [-1,0,1(这个1的索引是5)]
        #             [-1,0,1(这个1的索引是4)]
        #             [-1,0,1(这个1的索引是3)]
        #             所以为了避免这种情况：会一直移动右指针到3，此时nums[3](1) != nums[3-1](0),循环结束
        #             """
        #             while left_index < right_index and nums[right_index] == nums[right_index - 1]:
        #                 right_index -= 1
        #             # 避免重复，如果左指针的值与后一个值相等，左指针持续右移，持续找到不相等的值为止
        #             while left_index < right_index and nums[left_index] == nums[left_index + 1]:
        #                 left_index += 1
        #             # 移动左右指针
        #             left_index += 1
        #             right_index -= 1
        #         # 如果三数之和小于0，说明负数偏大，左指针右移
        #         elif nums[item] + nums[left_index] + nums[right_index] < 0:
        #             left_index += 1
        #         # 如果三数之和大于0，说明正数偏大，右指针左移
        #         else:
        #             right_index -= 1
        # print(result)
        # return result

        # 解法二：hashMap
        if not nums or len(nums) < 3:
            return []
        nums.sort()
        result = []
        # 最大值小于0或者或者最小值大于0，肯定不存在结果，为什么不取等号，因为避免出现元素均为0的情况
        if nums[0] > 0 or nums[len(nums) - 1] < 0:
            return result
        for item_i in range(len(nums) - 1):
            # 如果当前值指针值大于0且与上一个值相等，如果找到结果集也是重复集，故跳过本次循环
            if item_i > 0 and nums[item_i] == nums[item_i - 1]:
                continue
            # 这里就和两数之和逻辑一样，temp_map的元素均来自数组
            temp_map = {}
            for item_j in range(item_i + 1, len(nums)):
                # nums[item_i] + nums[item_j]和的负数是否存在于map中，如果存在，说明这三个元素
                # [nums[item_i], nums[item_j], -(nums[item_i] + nums[item_j])]组成一个结果集
                sum = temp_map.get(-(nums[item_i] + nums[item_j]), None)
                if sum:
                    # 这个地方去重一直不知道用什么好的方法
                    if not result.__contains__([nums[item_i], nums[item_j], -(nums[item_i] + nums[item_j])]):
                        result.append([nums[item_i], nums[item_j], -(nums[item_i] + nums[item_j])])
                # 如果不存在，将该数据放入Map,以备后续元素查询使用
                else:
                    temp_map[nums[item_j]] = 1
        return result


# print(Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4])
print(Solution().threeSum(nums=[0, 0, 0, 0]))
