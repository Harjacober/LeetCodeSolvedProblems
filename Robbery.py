def robbery(houses,i,memo): 
    if i<0: return 0
    if memo[i] != -1: return memo[i]
    maximum = 0 
    for j in range(i-2,-1,-1):
        maximum = max(maximum, robbery(houses,j,memo))
    memo[i] = maximum+houses[i] 
    return memo[i]

def solution(h):
    maxi = 0
    memo = [-1]*len(h) 
    for k in range(len(h)-1,-1,-1):
        maxi = max(maxi, robbery(h,k,memo)) 
    return maxi

arr = [1,3,5,1,2]
print(solution(arr))

#bottom up
def robbery2(arr):
    n = len(arr)
    dp = [0]*(n+2)
    for i in range(2,n+2):
        dp[i] = max(dp[i-2]+arr[i-2], dp[i-1])  
    return dp[-1]

print(robbery2(arr))
