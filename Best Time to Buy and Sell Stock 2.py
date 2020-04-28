#Top Down
def stock(k, arr, memo):
    if k<=0: return 0
    if memo[k] != -1: 
        return memo[k] 
    best = 0
    for i in range(k,-1,-1):
        profit = 0 if arr[k]-arr[i]<0 else arr[k]-arr[i]
        best = max(best, stock(i-1,arr,memo)+profit)

    memo[k] = best
    return memo[k]
def solution(arr):
    best = 0
    memo = [-1]*len(arr) 
    for i in range(len(arr)-1,-1,-1): 
        best = max(best, stock(i,arr,memo))

    return best

#Bottom up
def stock2(arr):
    n = len(arr)
    dp = [[0 for col in range(n)] for row in range(n)]
    for k,e in enumerate(arr):
        dp[0][k] = 0 if e-arr[0] < 0 else e-arr[0]
    for i in range(1,n):
        for j in range(i,n):
            profit = 0 if arr[j]-arr[i]<0 else arr[j]-arr[i]
            dp[i][j] = max(dp[i-1][i-1]+profit, dp[i-1][j])  
    return dp[n-1][n-1]

#Linear algorithm
def stock3(arr):
    valley,peak = arr[0],0
    maxprofit = 0
    i = 0
    while i < len(arr):
        valley = min(valley, arr[i])
        j = i
        while j+1<len(arr) and arr[j] >= peak:
            j+=1
        peak = arr[j]
        if arr[j] >= peak and peak>valley:
            maxprofit += (peak-valley) 
            i = j
        else: 
            valley = arr[j]
            peak = 0
        i += 1
    return maxprofit


a = [7,1,5,3,6,4]
print(stock3(a))
