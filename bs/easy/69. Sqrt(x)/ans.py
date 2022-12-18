class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        l,h=1,x//2
        res=1
        while l<=h:
            m=l+(h-l)//2
            if m==x//m: # m*m can cause overflow 2^30*2^30 > 2^31-1, won't overflow in python but is bad practice to ignore overflow
                return m
            elif m<x//m:
                res=m
                l=res+1
            else:
                h=m-1
        return res
