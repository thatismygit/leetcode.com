class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans=[-1]
        length=len(arr)
        max_count=ans[-1]
        for i in range(length-1,0,-1):
            if max_count<arr[i]:
                max_count=arr[i]
            ans.append(max_count)
        return ans[::-1]