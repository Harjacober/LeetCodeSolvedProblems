class NumArray:
    def __init__(self, nums):
        self.nums = nums
        ans = 0
        self.cache = [0]*len(nums)
        for i in range(len(nums)):
            ans += nums[i]
            self.cache[i] = ans

    def sumRange(self,i,j):
        if i == 0: return self.cache[j]
        return self.cache[j]-self.cache[i-1]

print(NumArray([-2,0,3,-5,2,-1]).sumRange(2,5))
[1,2,3,4]
[1,3,6,10]
[-2,-2,1,-4,-2,-3]
