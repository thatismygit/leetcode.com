# 0ms
class Solution:
    def climbStairs(self, n: int) -> int:
        def fun(n):
            if n <= 2:
                return n
            prev1, prev2 = 1, 2
            for i in range(n - 2):
                prev1, prev2 = prev2, (prev1 + prev2)
            return prev2

        return fun(n)
