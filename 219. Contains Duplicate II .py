# 48 ms
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums)==1: return False
        record=dict()
        for i in range(len(nums)):
            if nums[i] not in record:
                record[nums[i]]=[i]
                continue
            if len(record[nums[i]])==1:
                record[nums[i]].append(i)
                if (record[nums[i]][1]-record[nums[i]][0])<=k:
                    return True
                continue
            record[nums[i]][0]=record[nums[i]][1]
            record[nums[i]][1]=i
            if (record[nums[i]][1]-record[nums[i]][0])<=k:
                return True
        return False
