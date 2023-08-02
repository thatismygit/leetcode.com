class Solution:
    def maxArea(self, height: List[int]) -> int:
        count = len(height)
        left = 0
        right = count-1
        max_area=0
        while left<right:
            length = min(height[left],height[right])
            breath = right-left
            area = length * breath
            if area>max_area:
                max_area=area
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return max_area

# another solution

class Solution:
    def maxArea(self, height: List[int]) -> int:
        length=len(height)
        left,right=0,length-1
        max_area=0
        while left<right:
            length=min(height[left],height[right])
            breath=max(left,right)-min(left,right)
            area=(length*breath)
            if max_area<area:
                max_area=area
            if height[left]<height[right]:
                left+=1
            elif height[left]>height[right]:
                right-=1
            else:
                left+=1
                right-=1
        return max_area

# another solution

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        max_len=0
        while left<right:
            if height[left]<=height[right]:
                curr_len=height[left]*(right-left)
                left+=1
            else:
                curr_len=height[right]*(right-left)
                right-=1
            if max_len<curr_len:
                max_len=curr_len
        return max_len
