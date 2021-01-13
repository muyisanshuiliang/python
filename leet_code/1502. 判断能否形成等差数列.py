class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # 对数据进行排序
        arr.sort()
        # 两两计算元素之间的差
        a = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
        # 如果差值为一样的话值存在一个元素
        if len(set(a)) == 1:
            return True
        else:
            return False
