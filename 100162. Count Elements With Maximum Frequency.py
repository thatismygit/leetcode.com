class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hash_map=dict()
        for num in nums:
            if num in hash_map:
                hash_map[num]+=1
            else:
                hash_map[num]=1
        max_freq=max(hash_map.values())
        num_ele=0
        for i in hash_map.values():
            if i==max_freq:
                num_ele+=1
        return max_freq*num_ele