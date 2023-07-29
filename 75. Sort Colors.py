class Solution:
    def sortColors(self, nums: List[int]) -> None:
        length=len(nums)-1
        red,white,blue=0,0,length
        def swap(arr,clr1,clr2):
            nums[clr1],nums[clr2]=nums[clr2],nums[clr1]
        while white<=blue:
            if nums[white]==0:
                swap(nums,white,red)
                red+=1
            if nums[white]==2:
                swap(nums,white,blue)
                blue-=1
                white-=1
            white+=1


# another solution


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low,mid,high=0,0,len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                low+=1
            elif nums[mid]==2:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
                mid-=1
            mid+=1
