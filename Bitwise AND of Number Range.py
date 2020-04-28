from math import log,floor
# This algorithm is not correct
def bitwise(m,n):
    diff = n-m
    binary = list(bin(m)[2::])
    for j in range(len(binary)):
        if binary[j]=="1":
            a = len(binary)-1-j 
            factor = 2**a
            d = diff-(diff//factor)*factor 
            if diff+d>factor:
                binary[j]="0" 
    return int("".join(binary),2)&n 
        

print(bitwise(163524,163526))
