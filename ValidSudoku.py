 
def isvalidsudoku(board):
    ans = [] 
    for row in range(len(board)):
        r,c = [],[]
        for col in range(len(board)):
            if board[row][col] != ".":
                r.append(board[row][col])
            if board[col][row] != ".":    
                c.append(board[col][row])
        ans.append(r)
        ans.append(c)
    for i in range(0,9,3):
        for j in range(0,9,3):
            h = []
            for k in range(j,j+3):
                for e in board[k][i:i+3]:
                    if e != ".":
                        h.append(e)
            #print(h)            
            ans.append(h)
    print(ans)        
    isunique = lambda x : len(set(x)) == len(x)        
    for each in ans:
        if not isunique(each):
            return "false"
    return "true"    

arr = [["8","3",".",".","7",".",".",".","."],
       ["6",".",".","1","9","5",".",".","."],
       [".","9","8",".",".",".",".","6","."],
       ["8",".",".",".","6",".",".",".","3"],
       ["4",".",".","8",".","3",".",".","1"],
       ["7",".",".",".","2",".",".",".","6"],
       [".","6",".",".",".",".","2","8","."],
       [".",".",".","4","1","9",".",".","5"],
       [".",".",".",".","8",".",".","7","9"]]

print(isvalidsudoku(arr))
