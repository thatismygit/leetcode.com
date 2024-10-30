class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s==t or not s: return True
        if len(s)>len(t): return False
        i=0
        for ele in t:
            if ele == s[i]:
                i+=1
                if i==len(s):
                    return True
        return False