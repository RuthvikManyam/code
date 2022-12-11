class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=self.bs(nums,0,len(nums)-1,target)
        return res
    def firstocc(self,nums,k,target,res):
        while k>=0 and nums[k]==target:
            res[0]=k
            k-=1
        return 
    def lastocc(self,nums,k,target,res):
        while k<len(nums) and nums[k]==target:
            res[1]=k
            k+=1
        return
    def bs(self,nums,low,high,target):
        res=[-1,-1]
        while low<=high:
            m=low+(high-low)//2
            if nums[m]==target:
                self.firstocc(nums,m,target,res)
                self.lastocc(nums,m,target,res)
                return res
            elif nums[m]<target:
                low=m+1
            else:
                high=m-1
        return res
