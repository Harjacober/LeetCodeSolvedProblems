"""
calculate the maximum and minimum subarray sum.
The answer = max(maxSubarraySum, totalsum-minSubArraySum)
"""
def solution(arr): 
    currSumMax = maxSum = float('-inf')
    currSumMin = minSum = float('inf')
    total = 0
    for x in arr:
        currSumMin = min(x, currSumMin+x)
        currSumMax = max(x, currSumMax+x)
        maxSum = max(maxSum, currSumMax)
        minSum = min(minSum, currSumMin)
        total += x
        
    ans = max(maxSum, total-minSum)
    if ans == 0:
        return maxSum
    return ans 

a = [-5,-2,-5]
print(solution(a))
