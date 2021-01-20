"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

示例 1：
输入：target = 9
输出：[[2,3,4],[4,5]]

示例 2：
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
"""
from typing import List

from future.utils import lrange


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        if target == 0 or target == 1:
            return target
            # result = []
            # temp = []
            # temp_result = 0
            # # 由于题目中要求至少两个数之和，故此处只需对(target/2)以下的数据进行判断即可
            # # 15 // 2 == 7 ,(15 + 1) // 2 == 8，避免漏处理，故取后者
            # # rang(1,n) = [1,n)，故需要对上限+1
            # length = (target + 1) // 2 + 1
            # for item in reversed(range(1, length)):
            #     temp_result = temp_result + item
            #     temp.insert(0, item)
            #     if temp_result < target:
            #         continue
            #     else:
            #         if temp_result == target:
            #             append_temp = temp.copy()
            #             result.insert(0, append_temp)
            #         pop = temp.pop()
            #         temp_result = temp_result - pop
            # return result

        i = 1  # 滑动窗口的左边界
        j = 1  # 滑动窗口的右边界
        sum = 0  # 滑动窗口中数字的和
        res = []
        while i <= target // 2:
            if sum < target:
                # 右边界向右移动
                sum += j
                j += 1
            elif sum > target:
                # 左边界向右移动
                sum -= i
                i += 1
            else:
                # 记录结果
                arr = list(range(i, j))
                res.append(arr)
                # 左边界向右移动
                sum -= i
                i += 1
        return res


print(Solution().findContinuousSequence(15))
print(Solution().findContinuousSequence(1000))
print(Solution().findContinuousSequence(345))

