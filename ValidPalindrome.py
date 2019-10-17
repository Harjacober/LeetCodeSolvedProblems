def valid(s) -> bool:
    l,r = 0,len(s)-1 
    s = s.lower()
    i = 0 
    while l<r:
        if (not s[l].isalnum()): 
            l += 1
            continue
        elif (not s[r].isalnum()): 
            r -=1
            continue 
        elif s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True        

s = "  ab"            
print(valid(s))
