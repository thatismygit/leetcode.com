# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         return sum(set(nums))*2-sum(nums)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        length=len(nums)
        ans=nums[-1]
        for i in range(length-1):
            ans^=nums[i]
        return ans