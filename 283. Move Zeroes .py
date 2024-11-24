# 0ms
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if not len(nums) - 1:
            return nums
        l = 0
        for r in range(1, len(nums)):
            if not nums[l] and nums[r]:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
            elif nums[l]:
                l += 1
