class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # nums1 = nums1[:m]
        # nums1.extend(nums2[:n])
        # nums1.sort()
        # return nums1
        for item in list(range(n)):
            nums1[m+item] = nums2[item]
        nums1.sort()
        return nums1


print(list(range(5)))
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

solution = Solution()
print(solution.merge(nums1, m, nums2, n))
