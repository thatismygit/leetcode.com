class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        ans=list()
        for ele in arr2:
            cond1=ele in arr1
            cond2=ele in arr3
            if cond1 and cond2:
                ans.append(ele)
        return ans
