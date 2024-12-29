# via Recursion 242 ms

# class Solution:
#     def fib(self, n: int) -> int:
#         def fun(n):
#             if n==1 or n==2:
#                 return 1
#             return fun(n-1)+fun(n-2)
#         if n:
#             return fun(n)
#         return 0




# via Memoization 41 ms

# class Solution:
#     def fib(self, n: int) -> int:
#         def fun(n,memo={}):
#             if n==1 or n==2:
#                 return 1
#             if n not in memo:
#                 memo[n]=fun(n-1)+fun(n-2)
#             return memo[n]
#         if n:
#             return fun(n)
#         return 0




# via Tabualization 27ms


class Solution:
    def fib(self, n: int) -> int:
        def fun(n):
            if n == 1 or n == 2:
                return 1
            prev1, prev2 = 0, 1
            for i in range(n - 1):
                prev1, prev2 = prev2, (prev1 + prev2)
            return prev2

        if n:
            return fun(n)
        return 0
