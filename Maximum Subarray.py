def maxSubArray(arr):
    best = 0
    summ = 0
    for i in range(len(arr)):
        if summ<0 and arr[i]>summ:
            summ = arr[i]
        else:
            summ += arr[i]
        best = max(best, summ)
    return best

array = [-1,2,4,-3,5,2,-5,2]
print(maxSubArray(array))
    
