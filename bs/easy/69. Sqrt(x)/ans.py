class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        l,h=1,x//2
        res=1
        while l<=h:
            m=l+(h-l)//2
            if m**2==x:
                return m
            elif m**2<x:
                res=m
                l=res+1
            else:
                h=m-1
        return res
