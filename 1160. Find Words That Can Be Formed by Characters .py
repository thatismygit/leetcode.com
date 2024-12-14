# 303 ms
from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans=0
        for word in words:
            for char in Counter(word):
                if Counter(word)[char]>Counter(chars)[char]:
                    break
            else:
                ans+=len(word)
        return ans
