class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        start,end=0,0
        ans=0
        for start in range(len(word)-1):
            for end in range(start,len(word)):
                substring=word[start:end+1]
                cond1=all(ele in "aeiou" for ele in substring)
                cond2=all(ele in substring for ele in "aeiou")
                if cond1 and cond2:
                    ans+=1
        return ans
