class Solution(object):
    def breakfastNumber(self, staple, drinks, x):
        """
        :type staple: List[int]
        :type drinks: List[int]
        :type x: int
        :rtype: int
        """
        result = 0
        arr = [0 for _ in range(x + 1)]

        # 遍历食物，如果食物的价格小于指定价格
        for sta in staple:
            # 将当前食物价格的食物数量+1
            if sta < x:
                # 索引为食物的价格，值为该食物价格的数量
                arr[sta] += 1

        # 计算小于等于当前食物价格的食物总数
        for i in range(2, x):
            arr[i] += arr[i - 1]

        # 遍历饮料
        for drink in drinks:
            # 指定价格与食物之间的差值
            lt = x - drink
            # 如果差值为负，说明饮料的价格超标
            if lt <= 0:
                continue
            # 累计小于等于差值食物的数量，即可获取总组合数
            result += arr[lt]
        return result % (10 ** 9 + 7)


dict = {}
print(dict.get('1', 'c'))
staple = [10, 20, 5]
drinks = [5, 5, 2]
x = 15
solution = Solution()
print(solution.breakfastNumber(staple, drinks, 15))
