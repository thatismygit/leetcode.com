# 43ms
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = list()
        ans.append(s[: spaces[0]])
        for i in range(len(spaces) - 1):
            ans.append(s[spaces[i] : spaces[i + 1]])
        ans.append(s[spaces[len(spaces) - 1] :])
        return " ".join(ans)

