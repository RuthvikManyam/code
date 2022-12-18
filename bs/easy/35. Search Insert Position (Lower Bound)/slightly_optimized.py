class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.bs(nums,0,len(nums)-1,target)
    def bs(self,nums,low,high,target):
        while low<=high:
            m=low+(high-low)//2
            if nums[m]<=target:
                if nums[m]==target:
                    return m
                low=m+1 
            else:
                high=m-1
        return low  
