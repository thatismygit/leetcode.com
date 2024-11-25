# 0ms
class Solution:
    def reverseWords(self, s: str) -> str:
        ans=list(s.split(" "))
        for i in range(len(ans)):
            ans[i]=ans[i][::-1]
        return " ".join(ans)