def stock(b,s,array):
    if b==0: return arr[s]-arr[b] 
    return max(stock(b-1,s-1,array),
               stock(b-1,s,array),
               array[s]-array[b]) 


arr = [1]
n = len(arr)
#print(stock(n-2,n-1,arr))

#bottom up
def stock2(arr):
    m = len(arr)
    if n < 2: return 0
    dp = [[0 for j in range(m)]for i in range(m-1)]
    for k in range(m): 
        dp[0][k] = arr[k]-arr[0]
    for i in range(m):
        for j in range(m):
            if i<j and i>0:
                dp[i][j] = max(dp[i-1][j-1],
                               dp[i-1][j],arr[j]-arr[i])
 
    if dp[m-2][m-1] < 0: return 0
    else: return dp[m-2][m-1]

print(stock2(arr))

#one pass
import sys
def stock3(arr):
    minprice = sys.maxsize
    maxprofit = 0
    for i in range(n):
        if arr[i] < minprice: minprice = arr[i]
        elif profit[i]-minprice > maxprofit:
            maxprofit = profit[i]-minprice
    return maxprofit

print(stock3(arr))
                
                
            

