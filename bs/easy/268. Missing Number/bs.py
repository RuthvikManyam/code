class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l,h=0,len(nums)
        nums.sort()
        while l<h:
            m=l+(h-l)//2
            if nums[m]==m:
                l=m+1
            else:
                h=m
        return h
