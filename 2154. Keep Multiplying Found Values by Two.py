# 0ms
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = set(nums)
        for ele in nums:
            if original in nums:
                original = original << 1
                continue
            return original
        return original
