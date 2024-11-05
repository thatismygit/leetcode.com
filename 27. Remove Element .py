class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length=len(nums)
        if val not in nums: return length
        l,r=0,length-1
        while l<r:
            if nums[l]==val:
                while nums[r]==val:
                    r-=1
                    if l>=r: return l
                nums[l],nums[r]=nums[r],nums[l]
            l+=1
        return l