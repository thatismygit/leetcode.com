"""if opening parentheses add 0 in the stack

if closing parentheses and last of the stack is 0 then replace 0 with 1

if closing prantheses and last of stack is greater than 0 then pop it and multiply that value by 2

and check in every iteration if last two elements of stack are greater than 0 then add them together as one element
"""

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        from collections import deque
        stk=deque()
        for ele in s:
            if len(stk)>1:
                        if stk[-1]>0 and stk[-2]>0:
                            add=stk[-1]+stk[-2]
                            stk.pop()
                            stk.pop()
                            stk.append(add)
            if ele=="(":
                stk.append(0)
            else:
                if stk[-1]==0:
                    stk.pop()
                    stk.append(1)
                elif stk[-1]>0:
                    mul=stk.pop()
                    mul*=2
                    stk.pop()
                    stk.append(mul)
        return sum(stk)