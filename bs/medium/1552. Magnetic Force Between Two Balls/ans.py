class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l,r=1,position[-1]-position[0]
        res=1
        while l<=r:
            poss=l+(r-l)//2
            if self.helper(poss,position,m):
                res=poss
                l=poss+1
            else:
                r=poss-1
        return res

    def helper(self,poss,position,m):
        curr=1
        temp=position[0]
        for i in range(1,len(position)):
            if position[i]-temp>=poss:
                curr+=1
                temp=position[i]
        return curr>=m
