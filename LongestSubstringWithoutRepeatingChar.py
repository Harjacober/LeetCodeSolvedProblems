def lengthOfLongestSubstring(s): 
    if len(s)==0:
        return 0
    dic = { }
    start = 0
    maxx = 1
    b = True
    for i in range(len(s)): 
        if s[i] not in dic: 
            b = True
            dic[s[i]] = i
        elif dic[s[i]]<start:
            b = True
            dic[s[i]] = i
        else:
            b = False
            maxx = max(maxx, i-start) 
            start = dic[s[i]]+1 
            dic[s[i]] = i 
    if b:
        maxx = max(maxx, i-start+1) 
    return maxx

string = "tmmxvedtkm"
string2= "wejzbcmkkblrnktzqeugtjsrlajlvhsrldqmfeyrhkjw"
print(lengthOfLongestSubstring(string2))        
