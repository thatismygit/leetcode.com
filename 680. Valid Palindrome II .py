# 31 ms
# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         l,r=0,len(s)-1
#         while l<r:
#             if s[l]==s[r]:
#                 l+=1
#                 r-=1
#                 continue
#             elif (s[l]!=s[r] and s[l+1:r+1]==s[r:l:-1]) or (s[l]!=s[r] and s[l:r-1]==s[r-1:l:-1]): return True
#             return False
#         return True

# 27 ms
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
                continue
            return (s[l]!=s[r] and s[l+1:r+1]==s[r:l:-1]) or (s[l]!=s[r] and s[l:r-1]==s[r-1:l:-1])
        return True