import re
#using regex
def strstr(haystack, needle):
    pattern = re.compile(r'{}'.format(needle))
    match = re.search(pattern, haystack)
    if match:
        return match.span()[0]
    else:
        return -1

#withoutregex
def strstr2(haystack, needle):
    if len(needle)==0:
        return 0
    h,n,i = 0,0,0
    while h < len(haystack): 
        if haystack[h] != needle[n]:
            i += 1
            h = i
            n = 0
        else: 
            if n == len(needle)-1:
                return h-(len(needle)-1)
            h += 1
            n += 1
    return -1        
    

h = "mississippi"
n = "issip"
print(strstr2(h,n))    
    

           
