from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0

        # Initialize variables
        min_price = prices[0]
        max_profit = 0

        # Iterate through the prices
        for price in prices:
            # Update the minimum price
            if price < min_price:
                min_price = price

            # Update the maximum profit
            current_profit = price - min_price
            if current_profit > max_profit:
                max_profit = current_profit

        return max_profit



