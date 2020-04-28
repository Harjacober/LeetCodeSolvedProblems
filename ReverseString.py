def reverse(s):
    n = len(s)
    for i in range(n//2):
        temp = s[i]
        s[i] = s[n-i-1]
        s[n-i-1] = temp

    return s    

s = ["h","e","l","l","o"]
print(reverse(s))        
