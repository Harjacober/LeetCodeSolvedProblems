"""
The task is to flip the bits of num without leading zeros. let's flip the bits
with the leading zeros, i.e `flip = ~num`. after flipping the bits,we are only
interested in the first n bits where n is the number of bits of the original
number without the leading zero. n can be calculated as `n = floor(log(num))+1`.
Example: Given `num = 5 = 00000000000000000000000000000101`, `flip = 11111111111111111111111111111010`
we are only interested in the first 3bits in the flip whic is `010`.
One strategy to get the first 3bits in this case is to find a way to turn the remaining
from n+1 up till 32 to zero. we can turn all n+1 up till 32 `1s` to zero by anding
it with `0s` and retain the first n bits by andind it with `1s`. Thus we need `1 to n ones`
and `n+1 to 32 zeros`. we can achieve this by using the left shift binary operator on one.
i.e `((1<<n)-1)`. Simply doing `fnum & ((1<<n)-1)` will give us our answer
"""
from math import log,floor
def findComplement(num):
    #flip the bits including leading zeros
    fnum = ~num
    #get the number of active bits
    n = floor(log(num,2))+1
    
    return ((1<<n)-1) & fnum

def findComplement2(num): 
    #get the number of active bits
    n = floor(log(num,2))+1 
    return ((1<<n)-1) ^ num

if __name__ == '__main__': 
    assert 2 == findComplement(5)
    
