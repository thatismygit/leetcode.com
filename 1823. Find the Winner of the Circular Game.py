class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=list(range(1,n+1))
        index=0
        while len(arr)>1:
            index=(index+(k-1))%len(arr)
            arr.remove(arr[index])
        return arr[0]

# another solution

from collections import deque
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=deque(range(1,n+1))
        ele=0
        while len(arr)>1:
            j=k-1
            while j!=0:
                arr.append(arr.popleft())
                j-=1
            arr.popleft()
        return arr[0]
