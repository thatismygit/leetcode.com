class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s or max(s)<min(g): return 0
        g.sort()
        s.sort()
        i=0
        for cookie in s:
            greed=g[i]
            if cookie>=greed:
                i+=1
                if i>=len(g): return i
        return i
