# best time to buy and sell stock 121
class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit
prices=[2,4,1] 
print(Solution().maxProfit(prices))  