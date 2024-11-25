# 3ms
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if not len(nums) - 1:
            return nums
        l = 0
        for r in range(1, len(nums)):
            if (nums[l] & 1) and (not nums[r] & 1):
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                continue
            elif not nums[l] & 1:
                l += 1
                continue
        return nums

