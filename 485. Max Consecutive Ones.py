class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter=temp_counter=0
        length=len(nums)
        for i in range(length):
            if nums[i]==1:
                temp_counter+=1
            else:
                temp_counter=0
            if counter<temp_counter:
                counter=temp_counter
        return counter