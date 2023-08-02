class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        output = [-1] * len(nums)
        n = len(nums)
        stack = deque()
        for i in range(2 * len(nums) - 1, - 1, - 1):
            while stack and nums[i % n] >= stack[-1]:
                stack.pop()
            if stack:
                output[i % n] = stack[-1]
            stack.append(nums[i % n])
        return output

# another solution

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=deque()
        output=[-1]*len(nums)
        for i in range(2*len(nums) -1,-1,-1):
            i=i%len(nums)
            while stack and stack[-1]<=nums[i]:
                stack.pop()
            if stack:
                output[i]=stack[-1]
            stack.append(nums[i])
        return output
