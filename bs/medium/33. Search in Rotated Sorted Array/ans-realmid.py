class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        pivot=0
        while l<=r:
            m=l+(r-l)//2
            if nums[m]>nums[-1]:
                l=m+1
                pivot=l
            else:
                r=m-1
        l,r=0,len(nums)-1
        while l<=r:
            m=l+(r-l)//2
            rm=(m+pivot)%len(nums)
            if nums[rm]==target:
                return rm
            elif nums[rm]>target:
                r=m-1
            else:
                l=m+1
        return -1
