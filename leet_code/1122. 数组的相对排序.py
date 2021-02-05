#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1122. 数组的相对排序.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version
------------      -------               --------
2021/1/29 16:37   muyisanshuiliang      3.9

@Desciption:
------------------------------------------------------------
给你两个数组，arr1 和 arr2，
arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。

示例：
输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]
 
提示：
1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
arr2 中的元素 arr2[i] 各不相同
arr2 中的每个元素 arr2[i] 都出现在 arr1 中

'''

# import lib
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # if not arr1 or len(arr1) <= 1:
        #     return arr1
        # arr1.sort()
        # if not arr2 or len(arr2) <= 1:
        #     return arr1
        # temp = []
        # for item_inx, item_val in enumerate(arr2):
        #     while arr1.__contains__(item_val):
        #         temp.append(item_val)
        #         arr1.remove(item_val)
        # temp.extend(arr1)
        # return temp

        def memcomp(num):
            # 如果字典中索引值不存在，则返回本身
            return rank.get(num, num)

        n = len(arr2)
        # 根据arr2创建字典{值：索引}
        rank = {num: ind - n for ind, num in enumerate(arr2)}
        # 按照索引从小到大排序
        arr1.sort(key=memcomp)
        return arr1


print(Solution().relativeSortArray(arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]))
