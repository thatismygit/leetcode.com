# 4ms
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def fun(cost):
            curr=prev=0
            for i in range(2,len(cost)+1):
                prev,curr=curr,min(curr+cost[i-1],prev+cost[i-2])
            return curr
        if len(cost)==2:
            return min(cost)
        return fun(cost)
