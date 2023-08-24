class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low=curr_sum=0
        output=len(nums)+1
        flag=0
        for high in range(len(nums)):
            curr_sum+=nums[high]
            while curr_sum>=target:
                min_len=high-low
                output=min(output,min_len+1)
                curr_sum-=nums[low]
                low+=1
                flag+=1
        if flag:
            return output
        else:
            return 0