class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        large=sum(set(nums))*3
        small=sum(nums)
        return (large-small)//2

# another solution

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bucket=list()
        for i in range(len(nums)):
            ele=nums[i]
            if bucket.count(ele)<2:
                bucket+=[ele]
            else:
                bucket.remove(ele)
                bucket.remove(ele)
        return bucket[0]