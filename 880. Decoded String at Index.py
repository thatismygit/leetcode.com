class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        total=0
        count=list()
        for ele in s:
            if ele.isdigit():
                total*=int(ele)
                count.append(total)
            else:
                total+=1
                count.append(total)
        for index in range(len(s)-1,-1,-1):
            if count[index]<=k:
                if k%count[index]!=0:
                    k=k%count[index]
                else:
                    if s[index].isalpha():
                        return s[index]