# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         record=dict()
#         for i in range(len(nums)):
#             ele = nums[i]
#             if ele not in record:
#                 record[(target-ele)]=i
#                 continue
#             return [record[ele],i]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap=dict()
        for i in range(len(nums)):
            ele = nums[i]
            diff = target-nums[i]
            if ele in hashmap:
                ans = [hashmap[ele],i]
                return ans
            hashmap[diff]=i