# 88 ms
# class Solution:
#     def canMakeSubsequence(self, str1: str, str2: str) -> bool:
#         def next(ele):
#             if ele == "z":
#                 return "a"
#             return chr(ord(ele) + 1)

#         i2 = 0
#         for i1 in range(len(str1)):
#             if str1[i1] == str2[i2]:
#                 if i2 + 1 < len(str2):
#                     i2 += 1
#                     continue
#                 return True
#             if next(str1[i1]) == str2[i2]:
#                 if i2 + 1 < len(str2):
#                     i2 += 1
#                     continue
#                 return True
#         return False

# 67 ms
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i2 = 0
        for i1 in range(len(str1)):
            if str1[i1] == str2[i2]:
                if i2 + 1 < len(str2):
                    i2 += 1
                    continue
                return True
            if chr(ord(str1[i1]) + 1) == str2[i2] or (
                str1[i1] == "z" and str2[i2] == "a"
            ):
                if i2 + 1 < len(str2):
                    i2 += 1
                    continue
                return True
        return False
