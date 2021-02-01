#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   239. 滑动窗口最大值.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/2/1 10:55   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。

示例 1：
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

示例 2：
输入：nums = [1], k = 1
输出：[1]

示例 3：
输入：nums = [1,-1], k = 1
输出：[1,-1]

示例 4：
输入：nums = [9,11], k = 2
输出：[11]

示例 5：
输入：nums = [4,-2], k = 2
输出：[4]
'''

# import lib
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if len(nums) <= k:
            return [max(nums)]
        result = []
        index_queue = deque()
        for item_inx, item_val in enumerate(nums):
            # 维护单调递减队列，队列里面存放的是当前元素索引值
            while index_queue.__len__() != 0 and nums[index_queue[-1]] < item_val:
                index_queue.pop()
            index_queue.append(item_inx)
            # 如果当前索引与起始索引之间的差值大于等于间隔数，队首元素出列
            if index_queue[0] <= item_inx - k:
                index_queue.popleft()
            # 如果当前索引与起始索引之间的差值大于间隔数，最大数入结果集
            if item_inx >= k - 1:
                result.append(nums[index_queue[0]])
        return result


nums = [1, -2, -4, 8, -2, 5, 3, 6, 7]
k = 3
print(nums[0])
print(nums)
print(Solution().maxSlidingWindow(nums, k))
print(Solution().maxSlidingWindow([1, -1], 1))
