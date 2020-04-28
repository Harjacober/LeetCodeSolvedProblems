#Top down
def stairs(n, arr,memo):
    if n < 1: return 0
    if memo[n]!= -1:return memo[n]
    memo[n] = min(stairs(n-1,arr,memo)+arr[n-1], stairs(n-2,arr,memo)+arr[n-2])
    return memo[n]

array = [0,1,0,0,0,0]
n=len(array) 
print(stairs(len(array), array,[-1]*(n+2))) 
#bottom up
def stairs2(arr):
    arr.insert(0,0)
    arr.append(0) 
    n = len(arr)
    dp = [0]*(n)
    for i in range(1,n):
        dp[i] = min(dp[i-1]+arr[i-1], dp[i-2]+arr[i-2]) 
    return dp[-1]


inparr = [1,0,0,0] 
print(stairs2(inparr))
