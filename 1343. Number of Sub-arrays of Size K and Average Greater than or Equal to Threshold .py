# 251 ms
# class Solution:
#     def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
#         if k>threshold: return len(arr)-(k-1)
#         ans=0
#         for i in range(len(arr)-(k-1)):
#             if ((sum(arr[i:i+k])/k)>=threshold):
#                 ans+=1
#                 continue
#             continue
#         return ans

# 31 ms
# class Solution:
#     def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
#         if k>threshold: return len(arr)-(k-1)
#         ans,total=0,0
#         for i in range(k):
#             total+=arr[i]
#         if (total/k)>=threshold: ans+=1
#         for i in range(k,len(arr)):
#             total+=(arr[i]-arr[i-k])
#             if (total/k)>=threshold: ans+=1
#         return ans
    
# 32 ms
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if k>threshold: return len(arr)-(k-1)
        ans,total=0,sum(arr[:k])
        if (total/k)>=threshold: ans+=1
        for i in range(k,len(arr)):
            total+=(arr[i]-arr[i-k])
            if (total/k)>=threshold: ans+=1
        return ans
