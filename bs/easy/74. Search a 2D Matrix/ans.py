class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=self.bsu(matrix,0,len(matrix)-1,target)
        return self.bs(matrix[row],0,len(matrix[row])-1,target)

    def bsu(self,nums,low,high,target):
        while low<high:
            m=low+(high-low)//2
            if nums[m][-1]==target:
                return m
            elif nums[m][-1]<target:
                low=m+1
            else:
                high=m
        return high

    def bs(self,nums,low,high,target):
        while low<=high:
            m=low+(high-low)//2
            if nums[m]==target:
                return True
            elif nums[m]<target:
                low=m+1
            else:
                high=m-1
        return False

