class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        output=float("-inf")
        prefix=suffix=1
        length=len(nums)
        for i in range(length):
            prefix*=nums[i]
            suffix*=nums[length-i-1]
            output=max([output,nums[i],prefix,suffix])
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1
        return output