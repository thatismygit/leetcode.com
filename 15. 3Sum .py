# time exceed

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         length=len(nums)
#         ans=list()
#         for i in range(length):
#             l,r=i+1,length-1
#             while l<r:
#                 temp = [nums[i],nums[l],nums[r]]
#                 if sum(temp):
#                     if sum(temp)>0:
#                         r-=1
#                     else:
#                         l+=1
#                 else:
#                     if temp not in ans:
#                         ans.append(temp)
#                         continue
#                     r-=1
#         return ans