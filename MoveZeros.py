def movezeros(arr):
    i, j = 0, 0
    while i<len(arr):
        if arr[i] == 0:
            break
        i += 1
    for e in range(i+1,len(arr)):
        if arr[e] != 0:
            temp = arr[e]
            arr[i] = temp
            arr[e] = 0
            i+=1  
    return arr        

arr = [0,1,0,3,12,0,0,0,8,9,10,0,13,0]
print(movezeros(arr))            
