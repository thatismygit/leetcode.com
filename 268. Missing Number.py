class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums2=set(range(max(nums)+1))
        nums=set(nums)
        output=nums2.difference(nums)
        if len(output)==1:
            return output.pop()
        else:
            return max(nums)+1