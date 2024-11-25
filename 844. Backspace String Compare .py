# 0ms
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ans = [[], []]
        for ele in s:
            if ele != "#":
                ans[0].append(ele)
                continue
            if ans[0]:
                ans[0].pop()
        for ele in t:
            if ele != "#":
                ans[1].append(ele)
                continue
            if ans[1]:
                ans[1].pop()
        return ans[0] == ans[1]
