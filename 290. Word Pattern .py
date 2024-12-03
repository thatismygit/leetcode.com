# 0 ms
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        record = {}
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in record:
                record[pattern[i]] = s[i]
                continue
            if record[pattern[i]] != s[i]:
                return False
        record = {}
        for i in range(len(s)):
            if s[i] not in record:
                record[s[i]] = pattern[i]
                continue
            if record[s[i]] != pattern[i]:
                return False
        return True
