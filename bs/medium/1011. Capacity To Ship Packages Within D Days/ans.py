class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,h=max(weights),sum(weights)
        res=sum(weights)
        while l<=h:
            m=l+(h-l)//2
            print(m)
            if self.calc(m,weights,days):
                res=m
                h=m-1
            else:
                l=m+1
        return res

    def calc(self,capacity,weight,days):
        curr=0
        for w in weight:
            curr+=w
            if curr<capacity:
                continue
            else:
                days-=1
                if curr==capacity:
                    curr=0
                else:
                    curr=w
        if curr>0:
            days-=1
        if days<0:
            return False
        return True
