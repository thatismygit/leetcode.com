class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right=0,0
        unique=dict()
        max_len=0
        while right<len(s):
            ele=s[right]
            if ele not in unique:
                unique[ele]=right
                right+=1
            else:
                if unique[ele]+1>left:
                    left=unique[ele]+1
                unique[ele]=right
                right+=1
            if max_len<(right-left):
                    max_len=(right-left)
        return max_len
