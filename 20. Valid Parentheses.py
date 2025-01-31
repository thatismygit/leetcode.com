class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        stk=deque()
        close={")":"(","}":"{","]":"["}
        for ele in s:
            if len(stk)==0:
                stk.append(ele)
            elif ele in ")]}":
                if stk[-1]==close[ele]:
                    stk.pop()
                else:
                    stk.append(ele)
            else:
                stk.append(ele)
        if len(stk)==0:
            return True
        else:
            return False

# 3ms
class Solution:
    def isValid(self, s: str) -> bool:
        bucket = ""
        for i in range(len(s)):
            if s[i] in "([{":
                bucket += s[i]
                continue
            if not bucket:
                return False
            if s[i] == ")" and bucket[-1] == "(":
                bucket = bucket[:-1]
                continue
            if s[i] == "]" and bucket[-1] == "[":
                bucket = bucket[:-1]
                continue
            if s[i] == "}" and bucket[-1] == "{":
                bucket = bucket[:-1]
                continue
            return False
        if not bucket:
            return True
        return False
