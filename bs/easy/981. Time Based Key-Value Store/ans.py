class TimeMap:

    def __init__(self):
        self.time={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time:
            self.time[key] = []
        self.time[key].append([value,timestamp])
        return None

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time:
            return ""
        return self.bs(self.time[key],0,len(self.time[key])-1,timestamp)

    def bs(self,nums,l,h,target):
        res=""
        while l<=h:
            m=l+(h-l)//2
            if nums[m][1]==target:
                return nums[m][0]
            elif nums[m][1]<target:
                res=nums[m][0]
                l=m+1
            else:
                h=m-1
        return res
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
