# 5826 ms

# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         if len(nums)==1: return 0
#         if sum(nums[1:])==0: return 0
#         for i in range(1,len(nums)-1):
#             if sum(nums[:i])==sum(nums[i+1:]): return i
#         if sum(nums[:len(nums)-1])==0: return len(nums)-1
#         return -1

# 2 ms
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums)==1: return 0
        if len(nums)==2 and not nums[0] and not nums[1]: return 0
        lsum,rsum=0,sum(nums)
        for i in range(len(nums)):
            rsum-=nums[i]
            if lsum==rsum: return i
            lsum+=nums[i]
        return -1