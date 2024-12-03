# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         unique=deque()
#         count,max_count=0,0
#         for i in range(len(s)):
#             if s[i] not in unique:
#                 unique.appendleft(s[i])
#                 count+=1
#                 if max_count<count:
#                     max_count=count
#             else:
#                 poping=unique.pop()
#                 while poping!=s[i]:
#                     poping=unique.pop()
#                 unique.appendleft(s[i])
#                 count=len(unique)
#         return max_count

# another solution

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         left,right=0,0
#         unique=dict()
#         max_len=0
#         while right<len(s):
#             ele=s[right]
#             if ele not in unique:
#                 unique[ele]=right
#                 right+=1
#             else:
#                 if unique[ele]+1>left:
#                     left=unique[ele]+1
#                 unique[ele]=right
#                 right+=1
#             if max_len<(right-left):
#                     max_len=(right-left)
#         return max_len

# 11 ms
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, record = 0, list()
        for i in range(len(s)):
            if s[i] not in record:
                record.append(s[i])
                if len(record) > ans:
                    ans = len(record)
                continue
            record = record[record.index(s[i]) + 1 :]
            record.append(s[i])
        return ans
