class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
#       return [self.first(nums,0,len(nums)-1,target),self.last(nums,0,len(nums)-1,target)]
        return [self.comb(nums,0,len(nums)-1,target,1),self.comb(nums,0,len(nums)-1,target,0)]

    def comb(self,nums,low,high,target):
        res=-1
        while low<=high:
            m=low+(high-low)//2
            if nums[m]==target:
                res=m
                if flag:
                    high=m-1
                else:
                    low=m+1
            elif nums[m]<target:
                low=m+1
            else:
                high=m-1
        return res

    def first(self,nums,low,high,target):
        res=-1
        while low<=high:
            m=low+(high-low)//2
            if nums[m]==target:
                res=m
                high=m-1
            elif nums[m]<target:
                low=m+1
            else:
                high=m-1
        return res
    def last(self,nums,low,high,target):
        res=-1
        while low<=high:
            m=low+(high-low)//2
            if nums[m]==target:
                res=m
                low=m+1
            elif nums[m]<target:
                low=m+1
            else:
                high=m-1
        return res
    
