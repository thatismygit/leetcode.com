class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums)==1: return 0
        record=dict()
        if sum(nums[1:])==0: return 0
        for i in range(1,len(nums)-1):
            if sum(nums[:i])==sum(nums[i+1:]): return i
        if sum(nums[:len(nums)-1])==0: return len(nums)-1
        return -1
