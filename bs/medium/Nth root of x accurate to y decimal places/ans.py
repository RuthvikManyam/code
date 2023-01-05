class Solution:
    def NthRoot(self,num:float,n:int) -> float:
      if num==1 or n==1:
        return num
      l,r=1,num/n
      eps=0.01
      while abs(l-r)>eps:
        m=l+(r-l)/2
        temp=m**n
        if temp>x:
            r=x
        else:
            l=x
      return l
