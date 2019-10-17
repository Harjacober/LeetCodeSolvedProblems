def reverse(x):
    if x<0:
        g = True
    else:
        g = False
    ans = 0
    x = abs(x)
    while x:
        if g:
            last = -(x%10)
        else:
            last = x%10
        x //= 10 
        if (ans>(2**31-1)//10) or (ans == (2**31-1)//10 and last > 7):
            return 0
        if (ans<-(2**31//10)) or (ans == -(2**31//10) and last < -8):
            return 0
        ans = ans*10+last 
    return ans    

x = -1563847412
print(reverse(x))
