from collections import Counter
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        sort = sorted(counter.items(), key=lambda t: t[1])
        result = len(sort)
        for item in sort:
            if k >= item[1]:
                result -= 1
                k = k - item[1]
            else:
                break
        return result


print(Solution().findLeastNumOfUniqueInts(arr=[5, 5, 4], k=1))
print(Solution().findLeastNumOfUniqueInts(arr = [4,3,1,1,3,3,2], k = 3))
