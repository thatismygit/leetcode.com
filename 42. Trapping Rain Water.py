class Solution:
    def trap(self, height: List[int]) -> int:
        length=len(height)
        if length<=2: return 0
        l,r=0,length-1
        result=0
        max_l,max_r=height[l],height[r]
        while l<r:
            if max_l<=max_r:
                l+=1
                max_l=max(max_l,height[l])
                result+=max_l-height[l]
            else:
                r-=1
                max_r=max(max_r,height[r])
                result+=max_r-height[r]
        return result


# another solution

class Solution:
    def trap(self, height: List[int]) -> int:
        length=len(height)
        if length<=2: return 0
        l,r=0,length-1
        result=0
        max_l,max_r=height[l],height[r]
        while l<r:
            if max_l<=max_r:
                l+=1
                if max_l<height[l]:
                    max_l=height[l]
                result+=max_l-height[l]
            else:
                r-=1
                if max_r<height[r]:
                    max_r=height[r]
                result+=max_r-height[r]
        return result


# another solution

class Solution:
    def trap(self, height: List[int]) -> int:
        length=len(height)
        if length<=2: return 0
        l,r=0,length-1
        result=0
        max_l,max_r=height[l],height[r]
        while l<r:
            if max_l<=max_r:
                l+=1
                if max_l<height[l]:
                    max_l=height[l]
                else:
                    result+=max_l-height[l]
            else:
                r-=1
                if max_r<height[r]:
                    max_r=height[r]
                else:
                    result+=max_r-height[r]
        return result
