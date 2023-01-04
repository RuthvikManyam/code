class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        k=-1
        while l<=r:
            m=l+(r-l)//2
            if nums[m]>nums[-1]:
                k=m
                l=m+1
            else:
                r=m-1
        if k==-1:
            l,r=0,len(nums)-1
        else:
            if target in nums[:k+1]:
                l,r=0,k
            else:
                l,r=k+1,len(nums)-1
        while l<=r:
            m=l+(r-l)//2
            if nums[m]==target:
                return m
            elif nums[m]>target:
                r=m-1
            else:
                l=m+1
        return -1
