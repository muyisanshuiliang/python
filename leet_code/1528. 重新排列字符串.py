from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # 借助辅助空间
        # s_list = list(s)
        # if not s_list or len(s_list) == 0 or len(s_list) == 1:
        #     return s
        # result = ''
        # for item in list(range(len(indices))):
        #     find_index = indices.index(item)
        #     result = result + s_list[find_index]
        # return result

        # 原地交换
        s_list = list(s)
        if not s_list or len(s_list) == 0 or len(s_list) == 1:
            return s
        for item_inx, item_val in enumerate(s_list):
            if item_inx == indices[item_inx]:
                continue
            while True:
                if item_inx == indices[item_inx]:
                    break
                # 交换元素
                temp = s_list[item_inx]
                s_list[item_inx] = s_list[indices[item_inx]]
                s_list[indices[item_inx]] = temp

                # 交换索引
                temp = indices[indices[item_inx]]
                indices[indices[item_inx]] = indices[item_inx]
                indices[item_inx] = temp
        return ''.join(s_list)


solution = Solution()
print(solution.restoreString(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3]))
