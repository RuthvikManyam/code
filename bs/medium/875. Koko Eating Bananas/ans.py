class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while l<=r:
            k=l+(r-l)//2
            if self.caneat(k,piles,h):
                res=k
                r=k-1
            else:
                l=k+1
        return res
    
    def caneat(self,k,piles,h):
        for i in range(len(piles)):
            h-=piles[i]//k
            if piles[i]%k!=0:
                h-=1
            if h<0:
                return False
        return True
