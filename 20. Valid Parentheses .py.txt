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