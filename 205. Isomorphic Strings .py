class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash1=dict()
        hash2=dict()
        for i in range(len(s)):
            ele1=s[i]
            ele2=t[i]
            cond1 = s[i] not in hash1 and t[i] not in hash2
            cond2 = s[i] in hash1 and t[i] in hash2
            if cond1 or (cond2 and hash1[ele1] == hash2[ele2]):
                hash1[s[i]]=i
                hash2[t[i]]=i
                continue
            break
        else:
            return True
        return False