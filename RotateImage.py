def rotateimage(matrix):
    n = len(matrix)
    for layer in range(n//2):
        start = layer
        end = n-layer-1
        
        for j in range(end-layer):
            offset = n-start-1
            top = arr[start][start+j]
            arr[start][start+j] = arr[end-j][start]
            arr[end-j][start] = arr[offset][end-j]
            arr[offset][end-j] = arr[start+j][offset]
            arr[start+j][offset] = top
            print(matrix)

    return matrix


arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
print(rotateimage(arr))
    
