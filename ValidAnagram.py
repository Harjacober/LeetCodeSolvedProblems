def validanagram(s,t):
    arr = [0]*26
    for i in range(len(s)):
        arr[ord(s[i])-ord('a')] += 1
        arr[ord(t[i])-ord('a')] -= 1
    return (not any(arr))    

s = "anagram"
t = "nagarap"
print(validanagram(s,t))
