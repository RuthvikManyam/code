class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            m=l+(r-l)//2
            if m==0 or m==len(nums)-1 or (nums[m]!=nums[m-1] and nums[m]!=nums[m+1]):
                return nums[m]
            elif nums[m]==nums[m-1]:
                if (m-l)%2==0: 
                    r=m-2
                else:
                    l=m+1
            else:
                if (m-l)%2==0:
                    l=m+2
                else:
                    r=m-1
        return -1
