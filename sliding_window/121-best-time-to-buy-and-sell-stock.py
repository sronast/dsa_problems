class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        for i, p in enumerate(prices):
            if i == 0:
                continue
            if p<min_price:
                min_price = p
            
            else:
                profit = max(profit, p-min_price)
        return profit