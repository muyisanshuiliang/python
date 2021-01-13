import collections
import itertools
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # 统计词频{key=统计的词:val=词频}
        hash = collections.Counter(nums)
        # print(hash)
        # Counter({2: 3, 1: 2, 3: 1})
        # 对元素进行排序，根据词频升序，值降序(值，词频)
        # print(hash.items())
        sort = sorted(hash.items(), key=lambda t: (t[1], -t[0]))
        # print(sort)
        # 对列表进行舒展，由于只有两层，故只需舒展一次
        result = []
        for item in sort:
            result.extend([item[0]] * item[1])
        return result

        # return list(itertools.chain.from_iterable([[item[0]] * item[1] for item in sort]))


# print(Solution().frequencySort([1, 1, 2, 2, 2, 3, 4, 4]))
print(list(itertools.chain.from_iterable([[[1, 1], [2, 2]], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]])))
goodslist=[['Iphone', 5800], ['Mac Pro', 12000], ['Bike', 800], ['Alex Python', 89], ['Starbuck Latte', 30], ['Cap', 45], ['Air conditioning', 3000], [['Ipad'], 4200]]
list = [i for j in goodslist for i in j]
res = []