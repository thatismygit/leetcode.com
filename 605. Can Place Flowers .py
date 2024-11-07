class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # if it's not flowering anything condition it's itself satisfiable
        if not n: return True
        length=len(flowerbed)
        # for cases who's length is 1
        if length==1 and not flowerbed[0] and n==1:
            return True
        elif length==1:
            return False
        # for first index of flowerbed array
        if not flowerbed[0] and not flowerbed[1]:
            n-=1
            if not n: return True
            flowerbed[0]=1
        # for second index to second last index of flowerbed array
        for i in range(1,len(flowerbed)-2):
            if not flowerbed[i] and not flowerbed[i-1] and not flowerbed[i+1]:
                n-=1
                if not n: return True
                flowerbed[i]=1
        # for last index of flowerbed array
        if not flowerbed[length-1] and not flowerbed[length-2]:
            n-=1
            if not n: return True
        return False
