from itertools import groupby
def countandsay(n):
    val = "1"
    for i in range(n-1):
        arr = [] 
        for each,iterator in groupby(val):
            arr.append(str(len(list(iterator))))
            arr.append(each)
        val = ''.join(arr)
    return val        
    

print(countandsay(4))
