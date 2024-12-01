# 46 ms
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit=0
#         previous=prices[0]
#         for i in range(len(prices)):
#             if max_profit<(prices[i]-previous):
#                 max_profit=prices[i]-previous
#             if previous>prices[i]:
#                 previous=prices[i]
#         return max_profit

# 33 ms
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1: return 0
        ans=0
        low=0
        for high in range(1,len(prices)):
            if ans<(prices[high]-prices[low]):
                ans=prices[high]-prices[low]
            if prices[low]>prices[high]:
                low=high
        return ans