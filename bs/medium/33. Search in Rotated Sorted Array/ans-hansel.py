class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            m=l+(r-l)//2
            if nums[m]==target:
                return m
            elif nums[m]>=nums[l]:
                if nums[l]<=target and nums[m]>=target:
                    return self.bs(nums,target,l,m)
                else:
                    l=m+1
            else:
                if nums[m]<=target and nums[r]>=target:
                    return self.bs(nums,target,m,r)
                else:
                    r=m-1
        return -1

    def bs(self,nums,target,low,high):
        while low<=high:
            m=low+(high-low)//2
            if nums[m]==target:
                return m
            elif nums[m]>target:
                high=m-1
            else:
                low=m+1
        return -1
