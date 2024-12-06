# 0 ms
class Solution:
    def climbStairs(self, n: int) -> int:
        prev,prev2=2,1
        for i in range(2,n):
            prev2,prev=prev,(prev+prev2)
        if n==1: return 1
        return prev
