from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        if not A:
            return 0
        A.sort()
        r_inx = len(A) - 3
        while r_inx >= 0:
            if A[r_inx] + A[r_inx + 1] > A[r_inx + 2]:
                return sum(A[r_inx:r_inx + 3])
            else:
                r_inx -= 1
        return 0


print(Solution().largestPerimeter([3, 6, 2, 3]))