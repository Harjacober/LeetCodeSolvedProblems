#more efficient
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

def l2(s):
    dic = {s[0]:0}
    count, maxx = 1,1 
    i = 1
    while i < len(s): 
        if s[i] not in dic:
            count += 1
            dic[s[i]] = i
            i += 1
        else:
            i = dic[s[i]]+1
            dic.clear()  
            count = 0
        maxx = max(maxx, count)    
            
    return (maxx)        

string = "au"
string2= "wejzbcmkkblrnktzqeugtjsrlajlvhsrldqmfeyrhkjwtmbncvfmxvedtkpvggwrtwtwt"
print(lengthOfLongestSubstring(string2),l2(string2))        
