def plusOne(digit):
    i = len(digit)-1
    carry = 1
    while i >= 0:
        total = carry + digit[i] 
        carry = total//10
        rem = total%10
        digit[i] = rem
        if i == 0 and total>9:
            digit.insert(0,carry)
        i -= 1    
    return digit
digit = [9,9,9,9]
print(plusOne(digit))
