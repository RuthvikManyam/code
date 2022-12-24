class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        sorted(nums)
        l,r=1,max(nums)
        while l<=r:
            m=l+(r-l)//2
            if self.calc(m,nums,threshold):
                res=m
                r=m-1
            else:
                l=m+1
        return res

    def calc(self,m,nums,threshold):
        sum=0
        for n in nums:
            if n%m!=0:
                sum+=(n//m)+1
            else:
                sum+=n//m
        return sum<=threshold
