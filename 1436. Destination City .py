# 0 ms
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        rec, dest = dict(), paths[0][1]
        for i in range(1, len(paths)):
            if paths[i][0] == dest:
                dest = paths[i][1]
                continue
            if paths[i][0] not in rec:
                rec[paths[i][0]] = paths[i][1]
                continue
        while dest in rec:
            dest = rec[dest]
        return dest
