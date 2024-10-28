# class Solution:
#     def countPrimes(self, n: int) -> int:
#         ans=0
#         record=list(True for i in range(n))
#         p=2
#         while p*p<n:
#             if record[p]:
#                 for i in range(p*p,n,p):
#                     record[i]=False
#             p+=1
#         for i in range(2,n):
#             if record[i]:
#                 ans+=1
#         return ans

class Solution:
    def countPrimes(self, n: int) -> int:
        if not n or n==1:
            return 0
        record=list(1 for i in range(n))
        p=2
        while p*p<n:
            if record[p]:
                for i in range(p*p,n,p):
                    record[i]=0
            p+=1
        return sum(record)-2