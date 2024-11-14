# 3 ms

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length=len(flowerbed)
        if not n: return True
        if length==1 and not flowerbed[0] and n==1:
            return True
        elif length==1:
            return False
        if not flowerbed[0] and not flowerbed[1]:
            n-=1
            flowerbed[0]=1
            if not n: return True
        for i in range(1,len(flowerbed)-2):
            if not flowerbed[i] and not flowerbed[i-1] and not flowerbed[i+1]:
                n-=1
                flowerbed[i]=1
                if not n: return True
        if not flowerbed[length-1] and not flowerbed[length-2]:
            n-=1
            if not n: return True
        return False
# 7 ms

# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         # if it's not flowering anything condition it's itself satisfiable
#         if not n: return True
#         length=len(flowerbed)
#         # for cases who's length is 1
#         if length==1 and not flowerbed[0] and n==1:
#             return True
#         elif length==1:
#             return False
#         # for first index of flowerbed array
#         if not flowerbed[0] and not flowerbed[1]:
#             n-=1
#             flowerbed[0]=1
#             if not n: return True
#         # for second index to second last index of flowerbed array
#         for i in range(1,len(flowerbed)-2):
#             if not flowerbed[i] and not flowerbed[i-1] and not flowerbed[i+1]:
#                 n-=1
#                 flowerbed[i]=1
#                 if not n: return True
#         # for last index of flowerbed array
#         if not flowerbed[length-1] and not flowerbed[length-2]:
#             n-=1
#             if not n: return True
#         return False


# 8 ms

# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         # in the absence of target
#         if not n: return True

#         # incase length of flowerbed is 1
#         if len(flowerbed)==1:
#             if (flowerbed[0] and n) or (not flowerbed[0] and n>1): return False
#             return True
#         # placing flower at the begining of the plot
#         if not flowerbed[0] and not flowerbed[1]:
#             n-=1
#             flowerbed[0]=1
#         # placing flower at the end of the plot
#         if not flowerbed[-1] and not flowerbed[-2]: 
#             flowerbed[-1]=1
#             n-=1
#         # incase if target gets completed
#         if n<1: return True
#         # all the edge case of 2 length flowerplots are covered
#         if len(flowerbed)==2: return False
#         # iterating flowerbed array having atleast 3 in length 
#         i=1
#         while i<len(flowerbed)-1:
#             if not flowerbed[i] and not flowerbed[i-1] and not flowerbed[i+1]:
#                 n-=1
#                 if not n: return True
#                 flowerbed[i]=1
#                 i+=2
#                 continue
#             i+=1
#         return False