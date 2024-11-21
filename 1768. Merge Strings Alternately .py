# 39 ms
# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         w1, w2, ans = 0, 0, ""
#         while w1 < len(word1) or w2 < len(word2):
#             if w1 < len(word1) and w2 < len(word2):
#                 ans += word1[w1] + word2[w2]
#                 w1 += 1
#                 w2 += 1
#                 continue
#             elif w1 < len(word1):
#                 ans += word1[w1:]
#                 break
#             ans += word2[w2:]
#             break
#         return ans

# 40 ms
# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         ans = ""
#         limit = len(word1)
#         if len(word1) > len(word2):
#             limit = len(word2)
#         for i in range(limit):
#             ans += word1[i] + word2[i]
#         if len(word1) == len(word2):
#             return ans
#         if len(word1) > len(word2):
#             ans += word1[limit:]
#         if len(word1) < len(word2):
#             ans += word2[limit:]
#         return ans

# 30 ms
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        limit = len(word1)
        if len(word1) > len(word2):
            limit = len(word2)
        for i in range(limit):
            ans += word1[i] + word2[i]
        if len(word1) == len(word2):
            return ans
        if len(word1) > len(word2):
            ans += word1[limit:]
            return ans
        ans += word2[limit:]
        return ans
