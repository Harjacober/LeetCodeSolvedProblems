def rotate(nums, k):
    n = len(nums)
    a = nums*2 
    start = n-(k%n)
    end = start+n
    j = 0
    for i in range(start, end):
        nums[j] = a[i] 
        j += 1
    print(nums)
def approach2(nums, k):
    for i in range(k):
        a = nums.pop()
        nums.insert(0,a)
    print(nums)    
nums = [-1,-100,3,99]  
k = 4
#rotate(nums, k) 
approach2(nums, k)
