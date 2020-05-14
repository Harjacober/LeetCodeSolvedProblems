def maximalSquare(matrix):
    if not matrix: return 0
    m = len(matrix)
    n = len(matrix[0])
    best=0
    for i in range(m):
        for j in range(n):
            if matrix[i][j]=="1" and j>0 and i>0:
                val = 1 + min(int(matrix[i][j-1])
                              ,int(matrix[i-1][j]),
                              int(matrix[i-1][j-1]))
                matrix[i][j]=val
            else:
                val = int(matrix[i][j])

            best = max(best,val)

    return best**2 
                     
