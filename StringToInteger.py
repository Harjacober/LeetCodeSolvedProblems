def strtoint(s):
    i = 0
    mul = 1
    while i < len(s):
        if s[i].isdigit() or s[i] in ["+","-"]:
            if s[i] == "+":
                i += 1 
            elif s[i] == "-":
                i += 1
                mul = -1
            break
        else:
            if s[i] != ' ':
                return 0
        i += 1
    ans = 0    
    for j in range(i,len(s),1):
        if not s[j].isdigit():
            break
        val = int(s[j])*mul
        if (ans>(2**31-1)//10) or (ans == (2**31-1)//10 and val > 7):
            return 2**31-1
        if (ans<-(2**31//10)) or (ans == -(2**31//10) and val < -8):
            return -(2**31) 
        ans = ans*10 + val

    return ans          
#using regex
import re
def resolution(str):
    pattern = re.compile(r'(?:\s*)([+-]?\d+)')
    match = re.match(pattern, str.strip())
    if match:
        intt = int(match.group(1))
        if intt > 2**31-1:
            return 2**31-1
        elif intt < -(2**31):
            return (-2**31)
        else:
            return intt
    else:
        return 0
    
s = "42"
print(resolution(s))
