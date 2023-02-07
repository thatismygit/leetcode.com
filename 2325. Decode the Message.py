class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        #a-->97
        #z-->122
        alpha=dict()
        count=97
        for i in key:
            if i not in alpha and i !=" ":
                alpha[i]=chr(count)
                count+=1
        output=""
        for i in message:
            if i!=" ":
                output+=alpha[i]
            else:
                output+=i
        return output