# class Solution:
#     def maximumOddBinaryNumber(self, s: str) -> str:
#         if s.count("1")>1: return ("1"*(s.count("1")-1))+("0"*(len(s)-s.count("1")))+"1"
#         return ("0"*(len(s)-1))+"1"


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones=s.count("1")
        length=len(s)
        if ones>1: return ("1"*(ones-1))+("0"*(length-ones))+"1"
        return ("0"*(length-1))+"1"