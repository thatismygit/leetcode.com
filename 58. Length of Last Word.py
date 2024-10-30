class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # for checking the string with no whitespaces
        if len(s.split(" "))==1: return len(s)
        # iterating string from reverse order
        ans=str()
        for i in range(len(s)-1,-1,-1):
            if s[i]!=" ":
                ans+=s[i]
            elif ans:
                return len(ans)
        # if string have no white space in begining
        return len(ans)
