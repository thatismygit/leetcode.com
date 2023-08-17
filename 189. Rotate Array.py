class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length=len(nums)
        k%=len(nums)
        def reverse(l,r):
            if l<r:
                nums[l],nums[r]=nums[r],nums[l]
                return reverse(l+1,r-1)
        nums.reverse()
        reverse(0,k-1)
        reverse(k,length-1)