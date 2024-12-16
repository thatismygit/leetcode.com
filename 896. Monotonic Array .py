# 11 ms
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                continue
            break
        else:
            return True
        for i in range(1, len(nums)):
            if nums[i] >= nums[i - 1]:
                continue
            break
        else:
            return True
        return False
