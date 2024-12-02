# 251 ms
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if k>threshold: return len(arr)-(k-1)
        ans=0
        for i in range(len(arr)-(k-1)):
            if ((sum(arr[i:i+k])/k)>=threshold):
                ans+=1
                continue
            continue
        return ans
