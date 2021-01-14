from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) == 1:
            return intervals
        # 对元素的根据收个元素进行排序
        intervals.sort(key=lambda item: item[0])
        result = []
        pre = None
        max_index = len(intervals) - 1
        for item_inx, item_val in enumerate(intervals):
            # 第一次对前值赋值
            if pre is None:
                pre = item_val
            # 如果当前区间的第一个值大于前一区间的尾值，则分开放入列表
            elif item_val[0] > pre[1]:
                result.append(pre)
                pre = item_val
            else:
                # 否则对区间进行合并
                pre[1] = item_val[1] if item_val[1] > pre[1] else pre[1]
            # 最后一次,把最后一个元素追加到结果集中
            if item_inx == max_index:
                result.append(pre)
        return result


print(Solution().merge([[1, 3], [8, 10], [2, 6], [10, 18]]))