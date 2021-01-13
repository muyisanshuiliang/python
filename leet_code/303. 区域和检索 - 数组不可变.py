from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.__nums = nums
        self.__result = self.__get_result()
        print(self.__nums)
        print(self.__result)

    def sumRange(self, i: int, j: int) -> int:
        if j > len(self.__result):
            return self.__result[-1]
        return self.__result[j] - self.__result[(i - 1) if (i - 1) > 0 else 0]

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
