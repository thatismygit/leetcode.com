# 3 ms

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        records=Counter(text)
        return max([min([records["b"],records["a"],records["l"]//2,records["o"]//2,records["n"]]),0])
