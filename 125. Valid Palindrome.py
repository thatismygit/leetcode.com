class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        okay=[*range(97,123)]
        okay+=[*range(48,58)]
        while left<right:
            if (ord(s[left].lower()) in okay) and (ord(s[right].lower()) in okay):
                if s[left].lower()!=s[right].lower():
                    return False
                right-=1
                left+=1
            elif (ord(s[left].lower()) in okay):
                right-=1
            else:
                left+=1
        return True

# another solution

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left,right=0,len(s)-1
        while left<right:
            cond1=s[left].isalnum()
            cond2=s[right].isalnum()
            if (cond1 and cond2):
                if s[left].lower()==s[right].lower():
                    right-=1
                    left+=1
                    continue
                return False
            elif cond1:
                right-=1
            else:
                left+=1
        return True
