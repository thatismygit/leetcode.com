class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        left_over=money-(prices[1]+prices[0])
        if left_over>-1:
            return left_over
        return money
