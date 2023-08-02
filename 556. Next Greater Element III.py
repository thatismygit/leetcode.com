class Solution:
    def nextGreaterElement(self, n: int) -> int:
        lst=list(str(n))
        length=len(lst)
        dip=length-2
        while dip>-1:
            if lst[dip]>=lst[dip+1]:
                dip-=1
                continue
            break
        if dip==-1:
            return -1
        gtr_dip=length-1
        while gtr_dip>dip:
            if lst[dip]>=lst[gtr_dip]:
                gtr_dip-=1
                continue
            break
        lst[dip],lst[gtr_dip]=lst[gtr_dip],lst[dip]
        lst[dip+1:]=reversed(lst[dip+1:])
        ans=int("".join(lst))
        if ans.bit_length()>31:
            return -1
        return ans
