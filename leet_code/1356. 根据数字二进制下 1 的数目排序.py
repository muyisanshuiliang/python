from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        def count_one(num) -> {int: int}:
            count = 0
            temp = num
            if num == 0:
                return {num: count}
            while True:
                num = num & (num - 1)
                count += 1
                if num == 0:
                    return {temp: count}

        i = map(count_one, arr)
        print(list(i))


Solution().sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8])
