"""
编写一个 StockSpanner 类，它收集某些股票的每日报价，并返回该股票当日价格的跨度。
今天股票价格的跨度被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。
例如，如果未来7天股票的价格是 [100, 80, 60, 70, 60, 75, 85]，那么股票跨度将是 [1, 1, 1, 2, 1, 4, 6]。
"""


class StockSpanner:
    def __init__(self):
        self.__skip = []
        self.__prices = []

    def next(self, price: int) -> int:
        skip = 1
        # 如果是第一天或者今天的价格低于昨天的价格，跨度为1
        if len(self.__prices) == 0 or price < self.__prices[-1]:
            pass
        # 如果今天价格与昨天的价格相同，则跨度日在昨天的跨度上+1
        elif self.__prices[-1] == price:
            skip = self.__skip[-1] + skip
        else:
            skip_inx = len(self.__skip) - 1
            while skip_inx >= 0:
                if self.__prices[skip_inx] > price:
                    break
                # 获取昨天的跨度
                pre_skip = self.__skip[skip_inx]
                skip = skip + pre_skip
                skip_inx -= pre_skip

            while skip_inx >= 0:
                if self.__prices[skip_inx] <= price:
                    skip += 1
                    skip_inx -= 1
                else:
                    break
        self.__skip.append(skip)
        self.__prices.append(price)
        print(self.__prices)
        print(self.__skip)
        return skip


spanner = StockSpanner()
prices = [100, 87, 60, 70, 60, 75, 85, 86, 23, 24, 45, 74]
# prices = [31, 41, 48, 59, 79]
for item in prices:
    spanner.next(item)
