# 3 ms
# class Solution:
#     def largestGoodInteger(self, num: str) -> str:
#         ans = "-1"
#         for i in range(0, len(num) - 2):
#             if num[i] == num[i + 1] == num[i + 2] and int(ans) < int(num[i : i + 3]):
#                 ans = num[i : i + 3]
#         if ans == "-1":
#             return ""
#         return ans

# 0ms
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            if str(i) * 3 in num:
                return str(i) * 3
        return ""
