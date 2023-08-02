class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        mark=dict()
        max_count=0
        start,end=0,0
        while end<len(s):
            mark[s[end]]=end
            if len(mark)>2:
                mini=min(mark.values())
                start=mini+1
                del mark[s[mini]]
            count=(end-start)+1
            if max_count<count:
                max_count=count
            end+=1
        return max_count
