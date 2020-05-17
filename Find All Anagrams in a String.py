def findAnagrams(s, p):
    size = len(p)
    cache = [0]*26
    def isAnagram(s,p): 
        for i in range(len(p)):
            cache[ord(p[i])-ord('a')] += 1 
            cache[ord(s[i])-ord('a')] -= 1
        return not any(cache)

    ans = []
    j = 0
    flag = True
    while j+size <= len(s):
        if flag: 
            if isAnagram(s[j:j+size],p):
                ans.append(j)
            flag = False
        else:
            cache[ord(s[j-1])-ord('a')] += 1
            cache[ord(s[j+size-1])-ord('a')] -= 1
            if not any(cache):
                ans.append(j) 
        j += 1
    return ans

if __name__=='__main__':
    s = "cbaebabacd"
    p = "abc"
    assert([0,6] == findAnagrams(s, p))
