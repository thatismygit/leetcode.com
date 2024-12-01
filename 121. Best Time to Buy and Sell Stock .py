# 46 ms
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        previous=prices[0]
        for i in range(len(prices)):
            if max_profit<(prices[i]-previous):
                max_profit=prices[i]-previous
            if previous>prices[i]:
                previous=prices[i]
        return max_profit
