# 0ms
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if not rowIndex:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        ans, curr = [1, 1], list()
        for i in range(rowIndex - 1):
            for j in range(1, len(ans)):
                curr.append((ans[j] + ans[j - 1]))
            curr.insert(0, 1)
            curr.append(1)
            ans, curr = curr, list()
        return ans
