# 4ms
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if not k - 1 and len(nums) == 1:
            return 0
        nums.sort()
        l = 0
        diff = list()
        while (l + (k - 1)) < len(nums):
            diff.append(nums[l + (k - 1)] - nums[l])
            l += 1
        return min(diff)

