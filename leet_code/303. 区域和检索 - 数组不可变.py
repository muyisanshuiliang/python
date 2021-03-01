"""
给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。
实现 NumArray 类：
NumArray(int[] nums) 使用数组 nums 初始化对象
int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）
 
示例：
输入：
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
输出：
[null, 1, -1, -3]
解释：
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
 
提示：
0 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= i <= j < nums.length
最多调用 104 次 sumRange 方法
"""

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.__nums = nums
        self.__result = self.__get_result()
        print(self.__result)

    def sumRange(self, i: int, j: int) -> int:
        j = j if j <= (len(self.__result) - 1) else (len(self.__result) - 1)
        if i == 0:
            return self.__result[j]
        # 包含起始节点。故进行减法计算之后，将起始节点加到结果中
        return self.__result[j] - self.__result[i] + self.__nums[i]

    def __get_result(self):
        if not self.__nums or len(self.__nums) == 0:
            return []
        result = [0] * len(self.__nums)
        for item_inx, item_val in enumerate(self.__nums):
            if item_inx == 0:
                result[item_inx] = item_val
            else:
                result[item_inx] = result[item_inx - 1] + item_val
        return result


array = NumArray([-2, 0, 3, -5, 2, -1])

print(array.sumRange(0, 2))
print(array.sumRange(2, 5))
print(array.sumRange(0, 5))
print(array.sumRange(0, 7))
