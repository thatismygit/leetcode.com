# from collections import deque
# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         length=len(nums)
#         l,r=0,length-1
#         ans=deque()
#         while l<=r:
#             if abs(nums[l])>abs(nums[r]):
#                 ans.appendleft(nums[l]*nums[l])
#                 l+=1
#                 continue
#             ans.appendleft(nums[r]*nums[r])
#             r-=1
#         return list(ans)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length=len(nums)
        l,r=0,length-1
        ans=[0]*length
        i=length-1
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                ans[i]=nums[l]*nums[l]
                l+=1
                i-=1
                continue
            ans[i]=nums[r]*nums[r]
            r-=1
            i-=1
        return ans