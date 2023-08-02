class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        flag=False
        for i in range(len(word)):
            if word[i]==ch:
                flag=True
                break
        if flag==False:
            return word
        word=word[:i+1][::-1]+word[i+1:]
        return word

# another solution


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        present=len(word.split(ch))>1
        if present:
            rev_1=word.split(ch)[0]
            rev_1=ch+rev_1[::-1]
            wrd_2="".join(word[len(rev_1):])
            new_wrd=rev_1+wrd_2
            return new_wrd
        else:
            return word
