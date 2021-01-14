from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # 原始方法
        # 针对每个数字统计1的个数
        def count_one(num) -> [int, int]:
            # 用于统计1的数量
            count = 0
            temp = num
            if num == 0:
                return [num, count]
            while True:
                num = num & (num - 1)
                count += 1
                if num == 0:
                    return [temp, count]

        i = list(map(count_one, arr))

        # 先根据1的个数升序，再根据数据本身升序
        # sort = sorted(i, key=lambda t: (t[1], t[0]))
        i.sort(key=lambda t: (t[1], t[0]))
        # print(i)
        return [item[0] for item in i]

        # 骚操作,先根据1的个数升序，再根据数据本身升序
        # return sorted(arr, key=lambda x: (bin(x).count('1'), x))


print(Solution().sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]))
print(Solution().sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))

print(bin(-256))

