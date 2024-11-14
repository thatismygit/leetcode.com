# 63 ms

# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         ans=[-1]*len(nums1)
#         for i in range(len(nums1)):
#             if max(nums2[nums2.index(nums1[i]):len(nums2)])<nums1[i]: continue
#             for j in range(nums2.index(nums1[i])+1,len(nums2)):
#                 if nums2[j]>nums1[i]:
#                     ans[i]=nums2[j]
#                     break
#                 continue
#         return ans

# 19 ms
    
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count=dict()
        for i in range(len(nums2)):
            if nums2[i] not in nums1: continue
            for j in range(i+1,len(nums2)):
                if nums2[j]>nums2[i]:
                    count[nums2[i]]=nums2[j]
                    break
            else:
                count[nums2[i]]=-1
        ans=list()
        for i in range(len(nums1)):
            ans.append(count[nums1[i]])
        return ans