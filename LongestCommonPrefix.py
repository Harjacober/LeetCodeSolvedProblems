def matchingprefix(text1, text2):
    i,j = 0,0
    match = []
    while i<len(text1) and j<len(text2):
        if text1[i] != text2[j]:
            break
        match.append(text1[i])
        i +=1
        j += 1
 
    return "".join(match)    

def longestprefix(arr):
    if len(arr) < 1:
        return ""
    prefix = min(arr)
    for i in range(len(arr)): 
        prefix = matchingprefix(prefix, arr[i])
    return prefix

arr = []
print(longestprefix(arr))
