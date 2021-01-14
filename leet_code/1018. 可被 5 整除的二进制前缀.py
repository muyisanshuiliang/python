from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        result = []
        temp = 0
        for item_inx, item_val in enumerate(A):
            # 注意运算符的高低级（位运算符小于加法）
            temp = ((temp << 1) + item_val) % 5
            result.append(temp == 0)
        return result


print(Solution().prefixesDivBy5([0, 1, 1]))
