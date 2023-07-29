class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique=deque()
        count,max_count=0,0
        for i in range(len(s)):
            if s[i] not in unique:
                unique.appendleft(s[i])
                count+=1
                if max_count<count:
                    max_count=count
            else:
                poping=unique.pop()
                while poping!=s[i]:
                    poping=unique.pop()
                unique.appendleft(s[i])
                count=len(unique)
        return max_count
