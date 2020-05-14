def removeKdigits(num: str, k: int) -> str:
    ans = int(num)
    num = list(num)
    n = len(num)
    size = n-k 
    if size == 0: return "0"
    validArr = num[0:size]  
    for j in range(size, n):
        validArr.append(num[j])
        i = 0
        while i<len(validArr)-1:
            if int(validArr[i]) > int(validArr[i+1]):
                validArr.remove(validArr[i])
                break
            else:
                i += 1
        if len(validArr) > size:
            validArr.pop()
        ans = min(ans, int("".join(validArr)))

    return str(ans)

#using stack
def removeKdigitsStack(num: str, k: int) -> str:
    size = len(num)-k 
    stack = []
    for j in range(len(num)): 
        while stack and k and stack[-1]>num[j]:
            stack.pop()
            k -= 1
        stack.append(num[j])
    
    ans = stack[0:size]
    if ans:
        return str(int("".join(ans)))
    else:
        return "0"
        




if __name__ == '__main__':
    num = "10" 
    k = 2
    print(removeKdigitsStack(num, k))
    ans = removeKdigits(num, k) 
    assert("1219" == ans)