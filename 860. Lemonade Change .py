class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five,ten=0,0
        length=len(bills)
        for i in range(length):
            if bills[i]==5:
                five+=1
                continue
            elif bills[i]==10:
                if five:
                    five-=1
                    ten+=1
                    continue
                return False
            else:
                if ten and five:
                    five-=1
                    ten-=1
                    continue
                elif five>2:
                    five-=3
                    continue
                return False
        return True
