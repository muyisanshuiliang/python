from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # while nums.__contains__(val):
        #     nums.remove(val)
        # return len(nums)

        # 前后指针，把val全部移动到列表的末端，
        i, j = 0, len(nums)
        while i < j:
            if nums[i] == val:
                j = j - 1
                nums[j], nums[i] = nums[i], nums[j]
            else:
                i += 1
        else:
            # 循环退出的时候 i==j 返回i,j均可
            return j