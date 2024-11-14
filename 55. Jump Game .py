# 19 ms
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         max_jump=0
#         for i in range(len(nums)):
#             if max_jump<(i+nums[i]): max_jump=(i+nums[i])
#             if max_jump>=(len(nums)-1): return True
#             if max_jump==i: return False

# 120 ms
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length=len(nums)
        max_jump=0
        for i in range(length):
            if max_jump<(i+nums[i]): max_jump=(i+nums[i])
            if max_jump>=(length-1): return True
            if max_jump==i: return False