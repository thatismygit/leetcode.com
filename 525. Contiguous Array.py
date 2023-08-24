class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        bucket={0:-1}
        curr_sum=output=0
        for i in range(len(nums)):
            if nums[i]:
                curr_sum+=1
            else:
                curr_sum-=1
            if curr_sum in bucket:
                output=max(output,i-bucket[curr_sum])
            else:
                bucket[curr_sum]=i
        return output


# another solution with lower runtime

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        bucket={0:-1}
        curr_sum=output=0
        for i in range(len(nums)):
            if nums[i]:
                curr_sum+=1
            else:
                curr_sum-=1
            if curr_sum in bucket:
                if output<(i-bucket[curr_sum]):
                    output=i-bucket[curr_sum]
            else:
                bucket[curr_sum]=i
        return output
