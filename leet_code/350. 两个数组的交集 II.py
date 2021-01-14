from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # l1 = len(nums1)
        # l2 = len(nums2)
        # if l1 > l2:
        #     nums1, nums2 = nums2, nums1
        # result = []
        # for item in list(range(len(nums1) if len(nums1) <= len(nums2) else len(nums2))):
        #     nums1_val = nums1[item]
        #     if nums2.__contains__(nums1_val):
        #         result.append(nums1_val)
        #         nums2.remove(nums1_val)
        # return result

        l1 = len(nums1)
        l2 = len(nums2)
        if l1 > l2:
            nums1, nums2 = nums2, nums1
        counter_nums1 = dict(Counter(nums1))
        counter_nums2 = dict(Counter(nums2))
        result = []
        for item_key, item_val in counter_nums1.items():
            val = item_val if item_val <= counter_nums2.get(item_key, 0) else counter_nums2.get(item_key, 0)
            result.extend([item_key] * val)
        return result


print(Solution().intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
print(Solution().intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
