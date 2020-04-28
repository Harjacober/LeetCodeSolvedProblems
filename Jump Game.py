class Solution:
<<<<<<< HEAD
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
        
=======
    #recursive approach
    def canJumpRecursive(self, nums) -> bool:
        def helper(arr,pos,memo): 
            if pos >= len(arr)-1: return True 
            if memo[pos]!=0: return memo[pos]
            val = False
            for i in range(1,arr[pos]+1):
                #print(arr[pos],arr[pos+i])
                val = max(val,helper(arr,pos+i,memo))
            memo[pos] = val
            return memo[pos]
        memo = [0]*len(nums)
        print(helper(nums,0,memo))

    #Greedy solution
    def canJump(self, nums) -> bool:
        n = len(nums)
        currPos = n-1
        for i in range(n-2,-1,-1):
            if i+nums[i] >= currPos:
                currPos = i
        return currPos==0
        

a = [0]*1000
print(Solution().canJump(a))
>>>>>>> 7435d7724d8f64fc9efc8a6ea58c5cca383a1284
