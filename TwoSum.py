def twosum(nums, target):
    dic = {}
    for i in range(len(nums)):
        key = target-nums[i] 
        if key in dic:
            return [dic[key],i]
        else:
            dic[nums[i]] = i

nums = [-3,4,3,90]
target = 0
print(twosum(nums,target))            
