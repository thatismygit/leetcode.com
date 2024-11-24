#195ms
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         length=len(nums)
#         k%=len(nums)
#         def reverse(l,r):
#             if l<r:
#                 nums[l],nums[r]=nums[r],nums[l]
#                 return reverse(l+1,r-1)
#         nums.reverse()
#         reverse(0,k-1)
#         reverse(k,length-1)

# 6ms
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if not k:
            return nums
        k = len(nums) - k
        l, r = 0, k
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        l, r = k + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        l, r = 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums
