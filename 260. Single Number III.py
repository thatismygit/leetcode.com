class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bucket=list()
        for i in range(len(nums)):
            ele=nums[i]
            if ele not in bucket:
                bucket+=[ele]
            else:
                bucket.remove(ele)
        return bucket

# another solution

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bucket=Counter(nums)
        output=list()
        for ele in bucket:
            if bucket[ele]==1:
                output+=[ele]
        return output