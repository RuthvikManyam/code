def findbounds(nums,l,h,target):
    while nums[h]<target:
        l=h
        h=h*2
    return bs(nums,l,h,target)

def bs(nums,l,h,target):
    while l<=h:
        m=l+(h-l)//2
        if nums[m]==target:
            return m
        elif nums[m]<target:
            l=m+1
        else:
            h=m-1
    return -1

nums=[1,3,4,6,7,9,10,13,15]
target=10
print(findbounds(nums,0,1,target))
