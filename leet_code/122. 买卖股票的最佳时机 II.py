from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = 0
        max_price = 0
        for price in prices:
            if price < max_price:
                max_profit = max_price - min_price
                min_price = price
            else:
                max_price = max(price, max_price)

