class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=str()
        for i in range(len(min(strs))):
            temp=strs[0][i]
            for j in range(len(strs)):
                if temp!=strs[j][i]:
                    break
            else:
                ans+=temp
                continue
            return ans
        return ans
