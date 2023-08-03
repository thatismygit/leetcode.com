class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r=0,0
        add=nums[r]
        count=1
        max_count=count
        while l<=r and len(nums)>r:
            if nums[r]*(r+1-l)<=add+k:
                max_count=max(count,max_count)
                r+=1
                if len(nums)>r:
                    add+=nums[r]
                    count+=1
            else:
                add-=nums[l]
                l+=1
                count-=1
        return max_count
