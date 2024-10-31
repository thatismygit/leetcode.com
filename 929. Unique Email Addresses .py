# class Solution:
#     def numUniqueEmails(self, emails: List[str]) -> int:
#         unique=set()
#         for mail in emails:
#             temp=str()
#             local,domain=mail.split("@")
#             for l in local:
#                 if l==".":
#                     continue
#                 if l=="+":
#                     break
#                 temp+=l
#             temp+=("@"+domain)
#             unique.add(temp)
#         return len(unique)

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique=set()
        for mail in emails:
            local,domain=mail.split("@")
            # counting up "+"
            plus=local.count("+")
            if plus: local=local.split("+")[0]
            # counting up "."
            dots=local.count(".")
            for i in range(dots):
                local=local.replace(".","")
            unique.add(local+"@"+domain)
        return len(unique)