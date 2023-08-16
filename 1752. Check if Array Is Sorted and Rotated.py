class Solution:
    def check(self, nums: List[int]) -> bool:
        flag=1
        for i in range(len(nums)):
            if nums[i]<nums[i-1]:
                flag-=1
        if flag>=0:
            return True
        return False