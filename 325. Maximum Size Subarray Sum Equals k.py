class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        pre_sum=output=0
        bucket={}
        for i,num in enumerate(nums):
            pre_sum+=num
            if pre_sum==k:
                output=i+1
            if (pre_sum-k) in bucket:
                if output<(i-bucket[pre_sum-k]):
                    output=i-bucket[pre_sum-k]
            if not pre_sum in bucket:
                bucket[pre_sum]=i
        return output