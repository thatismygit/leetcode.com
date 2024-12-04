# 23 ms
# class Solution:
#     def fib(self, n: int) -> int:
#         def fibo_memo(n, memo={}):
#             if n <= 1:
#                 return n
#             if n not in memo:
#                 memo[n] = fibo_memo(n - 1) + fibo_memo(n - 2)
#             return memo[n]

#         return fibo_memo(n)

# 42 ms
# class Solution:
#     def fib(self, n: int) -> int:
#         def fibo_tabu(num):
#             if num<=1:
#                 return num
#             tabu=[0]*(num+1)
#             tabu[1]=1
#             for i in range(2,num+1):
#                 tabu[i]=tabu[i-1]+tabu[i-2]
#             return tabu[i]
#         return fibo_tabu(n)

# 34 ms
class Solution:
    def fib(self, n: int) -> int:
        def fib_tabu(num):
            if num<=1:
                return num
            prev,prev2=0,1
            for i in range(2,num+2):
                prev2,prev=prev,(prev+prev2)
            return prev
        return fib_tabu(n)