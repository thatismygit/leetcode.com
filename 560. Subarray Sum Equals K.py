class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output,curr_sum=0,0
        bucket={0:1}
        for i in nums:
            curr_sum+=i
            ele=curr_sum-k
            output+=bucket.get(ele,0)
            bucket[curr_sum]=1+bucket.get(curr_sum,0)
        return output