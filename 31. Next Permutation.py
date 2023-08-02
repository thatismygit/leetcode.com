class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)
        dip=n-2
        while dip>-1 and nums[dip]>=nums[dip+1]:
            dip-=1
        s_dip=n-1
        while s_dip>dip and nums[s_dip]<=nums[dip]:
            s_dip-=1
        nums[dip],nums[s_dip]=nums[s_dip],nums[dip]
        nums[dip+1:]=reversed(nums[dip+1:])
        if dip==-1:
            nums.sort()
