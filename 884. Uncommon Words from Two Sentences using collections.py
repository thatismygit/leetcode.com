class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        from collections import Counter
        s1=s1.split(" ")
        s2=s2.split(" ")
        d1=Counter(s1)
        d2=Counter(s2)
        output=list()
        for ele in d1:
            if d1[ele]==1 and ele not in d2:
                output.append(ele)
        for ele in d2:
            if d2[ele]==1 and ele not in d1:
                output.append(ele)
        return output