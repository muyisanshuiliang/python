"""
给你一个数组 favoriteCompanies ，其中 favoriteCompanies[i] 是第 i 名用户收藏的公司清单（下标从 0 开始）。
请找出不是其他任何人收藏的公司清单的子集的收藏清单，并返回该清单下标。下标需要按升序排列。

示例 1：
输入：favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
输出：[0,1,4]
解释：
favoriteCompanies[2]=["google","facebook"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 的子集。
favoriteCompanies[3]=["google"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 和 favoriteCompanies[1]=["google","microsoft"] 的子集。
其余的收藏清单均不是其他任何人收藏的公司清单的子集，因此，答案为 [0,1,4] 。

示例 2：
输入：favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
输出：[0,1]
解释：favoriteCompanies[2]=["facebook","google"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 的子集，因此，答案为 [0,1] 。

示例 3：
输入：favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
输出：[0,1,2,3]

提示：
1 <= favoriteCompanies.length <= 100
1 <= favoriteCompanies[i].length <= 500
1 <= favoriteCompanies[i][j].length <= 20
favoriteCompanies[i]中的所有字符串各不相同 。
用户收藏的公司清单也各不相同，也就是说，即便我们按字母顺序排序每个清单， favoriteCompanies[i] != favoriteCompanies[j] 仍然成立。
所有字符串仅包含小写英文字母。
"""
from typing import List


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        # if len(favoriteCompanies) <= 1:
        #     return [len(favoriteCompanies)]
        # temp = favoriteCompanies.copy()
        # temp.sort(key=len, reverse=True)
        # print(temp)
        # result = []
        # for item_inx, item_val in enumerate(temp):
        #     temp_index = 0
        #     while temp_index < item_inx:
        #         val_ = set(item_val) - set(temp[temp_index])
        #         if not val_:
        #             break
        #         temp_index += 1
        #     else:
        #         result.append(favoriteCompanies.index(item_val))
        #     result.sort()
        # return result

        # 获取内部元素最长的长度
        max_len = 1
        for lis in favoriteCompanies:
            max_len = max(max_len, len(lis))
        # 变成去重的集合
        favoriteCompanies = [set(x) for x in favoriteCompanies]
        n, res = len(favoriteCompanies), []
        for i in range(n):
            cur_set = favoriteCompanies[i]
            # 由于favoriteCompanies中的所有元素都不相等，所以一旦元素的长度达到最大长读，则该元素一定与其他的不一样
            if len(cur_set) == max_len:
                res.append(i)
                continue
            # 结果集追加标志位，默认是True
            flag = True
            # 遍历集合中的每一个元素
            for j in range(n):
                contrast_set = favoriteCompanies[j]
                # 遍历的元素索引与当前索引一直，不进行差集计算
                # 如果当前元素的长度大于遍历的元素，不进行差集计算
                if i == j or len(cur_set) >= len(contrast_set):
                    continue
                # 如果set1是set2的自己，则修改标志位置为False,循环结束
                if cur_set <= contrast_set:
                    flag = False
                    break
            if flag:
                res.append(i)
        return res


favoriteCompanies = [
    # 0
    ["leetcode", "google", "facebook"],
    # 1
    ["google", "microsoft"],
    # 2 1的子集
    ["google", "facebook"],
    # 3 0/1/2的子集
    ["google"],
    # 4 8的子集
    ["arrtztkotazhufrsfczr", "knzgidixqgtnahamebxf", "zibvccaoayyihidztflj"],
    # 5
    ["cffiqfviuwjowkppdajm", "owqvnrhuzwqohquamvsz"],
    # 6 8的子集
    ["knzgidixqgtnahamebxf", "owqvnrhuzwqohquamvsz", "qzeqyrgnbplsrgqnplnl"],
    # 7
    ["arrtztkotazhufrsfczr", "cffiqfviuwjowkppdajm"],
    # 8
    ["arrtztkotazhufrsfczr", "knzgidixqgtnahamebxf", "owqvnrhuzwqohquamvsz", "qzeqyrgnbplsrgqnplnl",
     "zibvccaoayyihidztflj"],
    # 9 与8相等
    ["arrtztkotazhufrsfczr", "knzgidixqgtnahamebxf", "owqvnrhuzwqohquamvsz", "qzeqyrgnbplsrgqnplnl",
     "zibvccaoayyihidztflj"]
]

print(Solution().peopleIndexes(favoriteCompanies))

set1 = set([2, 3])
set2 = set([2, 3, 4, 5])
print(set1 <= set2)
