class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total=nums[0]
        curr_sum=nums[0]
        for ele in nums[1:]:
            if (ele+curr_sum)>ele:
                curr_sum+=ele
            else:
                curr_sum=ele
            if total<curr_sum:
                total=curr_sum
        return total

# another solution

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=float("-inf")
        curr_sum=0
        length=len(nums)
        for i in range(length):
            ele=nums[i]
            curr_sum+=ele
            if curr_sum>max_sum:
                max_sum=curr_sum
            if curr_sum<0:
                curr_sum=0
        return max_sum