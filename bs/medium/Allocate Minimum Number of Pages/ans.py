class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,books, num_of_books, students):
        l,r=books[-1],sum(books)
        if students>len(books):
            return -1
        while l<=r:
            m=l+(r-l)//2
            if self.calc(m,books,students):
                res=m
                r=m-1
            else:
                l=m+1
        return res
        
    def calc(self,m,books,students):
        temp=0
        for b in books:
            if b>m:
                return False
            temp+=b
            if temp>m:
                temp=b
                students-=1
        if temp:
            students-=1
        return students>=0
