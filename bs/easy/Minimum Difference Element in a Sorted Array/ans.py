nums=[1,3,7,10,15]
target=12
l=lower(nums,0,len(nums)-1,target)
u=upper(nums,0,len(nums)-1,target)
if target-nums[l]<=nums[u]-target:
    return nums[l]
else:
    return nums[u]

def lower(nums,0,len(nums)-1,target):
    while low<=high:
        m=low+(high-low)//2
        if nums[m]==target:
            return m
        elif nums[m]<target:
            low=m-1
        else:
            high=m+1
    return low
    
def upper(nums,0,len(nums)-1,target):
    while low<high:
        m=low+(high-low)//2
        if nums[m]==target:
            return 0
        elif nums[m]<target:
            return low=m-1
        else:
            high=m
    return high
