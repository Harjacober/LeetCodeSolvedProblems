def minSubArrayLen(s: int, nums) -> int:
        count = 1
        j = 0
        target = 0
        ans = []
        for i in range(len(nums)):
            target += nums[i]
            while target >= s:
                print(target, count)
                ans.append(count)
                target -= nums[j]
                j += 1
                count -=1
            count += 1 
        if ans:    
            print(ans)
            return min(ans)
        else:
            return 0
            
s = 5
nums = [2,3,1,2,4,3]
print(minSubArrayLen(s, nums))
