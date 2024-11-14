class Solution:
    def maxDepth(self, s: str) -> int:
        depth,ans=0,0
        for ele in s:
            if ele in "(":
                depth+=1
                if depth>ans: ans=depth
                continue
            elif ele in ")":
                depth-=1
                continue
        return ans
