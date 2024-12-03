class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        record=set()
        for ele in arr:
            if ele not in record:
                if ele&1: # for odd number
                    record.add(ele*2)
                    continue
                record.add(ele*2) # for even number
                record.add(ele//2)
                continue
            return True
        return False
