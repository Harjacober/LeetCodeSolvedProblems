def palindrome(string):
    n = len(string)
    maxx = 0
    ans = 0,0
    dic = {e:1 for e in string} 
    for i in range(n-1,-1,-1):
        substring = ""
        for j in range(i+1,n): 
            if string[i] == string[j]: 
                if substring in dic:
                    if dic[substring]+2 > maxx:
                        ans = i,j
                        maxx = max(maxx, dic[substring]+2)
                    dic[string[i]+substring+string[j]] = dic[substring]+2
                else:
                    if substring == "":
                        if 2 > maxx:
                            ans = i,j
                        maxx = max(maxx, 2)
                        dic[string[i]+string[j]] = 2
                        
            substring += string[j]
            
        substring = ""

    return string[ans[0]:ans[1]+1]
            
print(palindrome("haaaad"))
