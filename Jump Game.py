class Solution:
    def canJump(self, nums) -> bool:
        j = len(nums)-1
        i = j-1
        while i>=0:
            steps = j-i
            if nums[i]>=steps:
                j=i
                i-=1 
            else:
                if i==0: return False 
                i-=1 
        return True

a = [9,0,0,0,0,4,0,0,0,7]
print(Solution().canJump(a))
        
